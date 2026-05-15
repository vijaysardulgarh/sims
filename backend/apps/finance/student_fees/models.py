# ============================================
# finance/student_fees/models.py
# ============================================

from django.db import models
from django.core.exceptions import ValidationError


class StudentFee(models.Model):

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="fees"
    )

    fee_structure = models.ForeignKey(
        "fee_structures.FeeStructure",
        on_delete=models.CASCADE,
        related_name="student_fees"
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    due_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    session = models.CharField(
        max_length=20,
        db_index=True
    )

    is_closed = models.BooleanField(
        default=False,
        db_index=True
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def clean(self):

        if self.total_amount < 0:
            raise ValidationError(
                "Total amount cannot be negative"
            )

        if self.paid_amount < 0:
            raise ValidationError(
                "Paid amount cannot be negative"
            )

        if self.paid_amount > self.total_amount:
            raise ValidationError(
                "Paid amount cannot exceed total"
            )

    def save(self, *args, **kwargs):

        # Auto populate
        if not self.pk and self.fee_structure:

            self.total_amount = (
                self.fee_structure.total_fee
            )

            self.session = (
                self.fee_structure.session
            )

        self.due_amount = (
            self.total_amount - self.paid_amount
        )

        self.is_closed = self.due_amount <= 0

        self.full_clean()

        super().save(*args, **kwargs)

    @property
    def payment_count(self):
        return self.payments.count()

    def __str__(self):
        return f"{self.student} - {self.session}"

    class Meta:
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["student", "session"],
                name="unique_student_fee"
            )
        ]
