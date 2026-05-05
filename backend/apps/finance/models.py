from django.db import models, transaction
from django.db.models import F, Q
from django.core.exceptions import ValidationError
from django.utils import timezone
import uuid


# =========================
# 📊 FEE STRUCTURE
# =========================
class FeeStructure(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE, related_name="fee_structures")
    class_obj = models.ForeignKey("Class", on_delete=models.CASCADE, related_name="fee_structures")
    stream = models.ForeignKey("Stream", on_delete=models.CASCADE, null=True, blank=True)

    session = models.CharField(max_length=20, db_index=True)

    admission_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rcf = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cwf = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ccwf = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    is_active = models.BooleanField(default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        fields = [self.admission_fee, self.rcf, self.cwf, self.ccwf, self.other_fee]
        if any(f < 0 for f in fields):
            raise ValidationError("Fee values cannot be negative")

    @property
    def total_fee(self):
        return (
            self.admission_fee +
            self.rcf +
            self.cwf +
            self.ccwf +
            self.other_fee
        )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.stream:
            return f"{self.class_obj} ({self.stream}) - {self.session}"
        return f"{self.class_obj} - {self.session}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["school", "class_obj", "stream", "session"],
                name="unique_fee_structure_per_session"
            )
        ]
        indexes = [
            models.Index(fields=["school", "class_obj"]),
            models.Index(fields=["session"]),
        ]
        ordering = ["-session", "class_obj"]


# =========================
# 🎓 STUDENT FEE (LEDGER)
# =========================
class StudentFee(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE, related_name="fees")
    fee_structure = models.ForeignKey("FeeStructure", on_delete=models.CASCADE, related_name="student_fees")

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)

    session = models.CharField(max_length=20, db_index=True)

    is_closed = models.BooleanField(default=False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.total_amount < 0:
            raise ValidationError("Total amount cannot be negative")

        if self.paid_amount < 0:
            raise ValidationError("Paid amount cannot be negative")

        if self.paid_amount > self.total_amount:
            raise ValidationError("Paid amount cannot exceed total")

    def save(self, *args, **kwargs):
        # Auto sync from fee structure if new
        if not self.pk and self.fee_structure:
            self.total_amount = self.fee_structure.total_fee
            self.session = self.fee_structure.session

        self.due_amount = self.total_amount - self.paid_amount
        self.is_closed = self.due_amount <= 0

        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.session}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "session"],
                name="unique_fee_per_student_per_session"
            )
        ]
        indexes = [
            models.Index(fields=["student"]),
            models.Index(fields=["session"]),
        ]
        ordering = ["-created_at"]


# =========================
# 💰 PAYMENT MODEL
# =========================
class FeePayment(models.Model):
    student_fee = models.ForeignKey("StudentFee", on_delete=models.CASCADE, related_name="payments")

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    PAYMENT_MODE_CHOICES = [
        ("Cash", "Cash"),
        ("Online", "Online"),
        ("Cheque", "Cheque"),
        ("UPI", "UPI"),
    ]
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES)

    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    receipt_number = models.CharField(max_length=50, unique=True, editable=False)

    payment_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("Payment amount must be greater than 0")

        if self.student_fee.is_closed:
            raise ValidationError("Fee is already fully paid")

        if self.pk:
            raise ValidationError("Existing payments cannot be modified")

    def save(self, *args, **kwargs):
        with transaction.atomic():
            is_new = self.pk is None

            self.full_clean()

            if is_new and not self.receipt_number:
                self.receipt_number = f"RCPT-{uuid.uuid4().hex[:10].upper()}"

            if is_new:
                student_fee = StudentFee.objects.select_for_update().get(pk=self.student_fee.pk)

                if student_fee.is_closed:
                    raise ValidationError("Fee already paid")

                if self.amount > student_fee.due_amount:
                    raise ValidationError("Payment exceeds due amount")

                student_fee.paid_amount = F('paid_amount') + self.amount
                student_fee.save()
                student_fee.refresh_from_db()

            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_fee.student} paid {self.amount}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["transaction_id"],
                condition=Q(transaction_id__isnull=False),
                name="unique_transaction_id"
            )
        ]
        indexes = [
            models.Index(fields=["payment_date"]),
        ]
        ordering = ["-created_at"]