from django.db import models

from django.db.models import (
    Q
)

from django.core.exceptions import (
    ValidationError
)

from apps.schools.models import School
from apps.students.models import Student
from apps.finance.fee_structures.models import FeeStructure

class StudentFee(models.Model):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="student_fees",
        db_index=True
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="fees",
        db_index=True
    )

    fee_structure = models.ForeignKey(
        FeeStructure,
        on_delete=models.CASCADE,
        related_name="student_fees",
        db_index=True
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

    class Meta:

        ordering = [
            "-created_at"
        ]

        indexes = [

            models.Index(
                fields=["session"]
            ),

            models.Index(
                fields=["school"]
            ),

            models.Index(
                fields=["is_closed"]
            ),
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "student",
                    "session"
                ],
                name="unique_student_fee"
            ),

            models.CheckConstraint(
                condition=Q(total_amount__gte=0),
                name="student_fee_total_positive"
            ),

            models.CheckConstraint(
                condition=Q(paid_amount__gte=0),
                name="student_fee_paid_positive"
            ),

            models.CheckConstraint(
                condition=Q(due_amount__gte=0),
                name="student_fee_due_positive"
            ),
        ]

    def clean(self):

        if self.total_amount < 0:

            raise ValidationError({
                "total_amount":
                    (
                        "Total amount cannot "
                        "be negative"
                    )
            })

        if self.paid_amount < 0:

            raise ValidationError({
                "paid_amount":
                    (
                        "Paid amount cannot "
                        "be negative"
                    )
            })

        if (
            self.paid_amount >
            self.total_amount
        ):

            raise ValidationError({
                "paid_amount":
                    (
                        "Paid amount cannot "
                        "exceed total amount"
                    )
            })

    def save(self, *args, **kwargs):

        if (
            not self.pk and
            self.fee_structure
        ):

            self.total_amount = (
                self.fee_structure.total_fee
            )

            self.session = (
                self.fee_structure.session
            )

            self.school = (
                self.fee_structure.school
            )

        self.due_amount = (
            self.total_amount -
            self.paid_amount
        )

        self.is_closed = (
            self.due_amount <= 0
        )

        self.full_clean()

        super().save(*args, **kwargs)

    @property
    def payment_count(self):

        return (
            self.payments.count()
        )

    def __str__(self):

        return (
            f"{self.student} "
            f"- "
            f"{self.session}"
        )