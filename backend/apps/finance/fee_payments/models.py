# ============================================
# finance/fee_payments/models.py
# ============================================

from django.db import models, transaction
from django.db.models import F
from django.core.exceptions import ValidationError
from django.utils import timezone
import uuid


class FeePayment(models.Model):

    PAYMENT_MODE_CHOICES = [
        ("Cash", "Cash"),
        ("UPI", "UPI"),
        ("Online", "Online"),
        ("Cheque", "Cheque"),
    ]

    student_fee = models.ForeignKey(
        "student_fees.StudentFee",
        on_delete=models.CASCADE,
        related_name="payments"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_mode = models.CharField(
        max_length=20,
        choices=PAYMENT_MODE_CHOICES
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    receipt_number = models.CharField(
        max_length=50,
        unique=True,
        editable=False
    )

    payment_date = models.DateField(
        default=timezone.now
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def clean(self):

        if self.amount <= 0:
            raise ValidationError(
                "Payment amount must be greater than 0"
            )

        if self.student_fee.is_closed:
            raise ValidationError(
                "Fee already fully paid"
            )

        if (
            self.amount >
            self.student_fee.due_amount
        ):
            raise ValidationError(
                "Payment exceeds due amount"
            )

    def save(self, *args, **kwargs):

        with transaction.atomic():

            is_new = self.pk is None

            self.full_clean()

            if is_new and not self.receipt_number:

                self.receipt_number = (
                    f"RCPT-"
                    f"{uuid.uuid4().hex[:10].upper()}"
                )

            super().save(*args, **kwargs)

            if is_new:

                student_fee = (
                    self.student_fee
                )

                student_fee.paid_amount = (
                    F("paid_amount") + self.amount
                )

                student_fee.save()

                student_fee.refresh_from_db()

    def __str__(self):

        return (
            f"{self.student_fee.student} "
            f"paid {self.amount}"
        )

    class Meta:
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["payment_date"]),
        ]