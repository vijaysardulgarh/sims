import uuid

from django.db import (
    models,
    transaction
)

from django.db.models import (
    F,
    Q
)

from django.core.exceptions import (
    ValidationError
)

from django.utils import timezone

from apps.finance.student_fees.models import StudentFee
from apps.schools.models import School
from apps.accounts.users.models import User
from apps.core.common.base.models import SchoolBaseModel

class FeePayment(SchoolBaseModel):

    PAYMENT_MODE_CHOICES = [

        ("Cash", "Cash"),

        ("UPI", "UPI"),

        ("Online", "Online"),

        ("Cheque", "Cheque"),
    ]

    PAYMENT_STATUS_CHOICES = [

        ("Pending", "Pending"),

        ("Success", "Success"),

        ("Failed", "Failed"),

        ("Refunded", "Refunded"),
    ]

    student_fee = models.ForeignKey(
        StudentFee,
        on_delete=models.CASCADE,
        related_name="payments",
        db_index=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_mode = models.CharField(
        max_length=20,
        choices=PAYMENT_MODE_CHOICES
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="Success"
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    receipt_number = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
        db_index=True
    )

    payment_date = models.DateField(
        default=timezone.now
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_fee_payments"
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
                fields=["payment_date"]
            ),

            models.Index(
                fields=["receipt_number"]
            ),

            models.Index(
                fields=["school"]
            ),
        ]

        constraints = [

            models.CheckConstraint(
                condition=Q(amount__gt=0),
                name="fee_payment_amount_positive"
            )
        ]

    def clean(self):

        if self.amount is None or self.amount <= 0:

            raise ValidationError({
                "amount":
                    (
                        "Payment amount must "
                        "be greater than 0"
                    )
            })

        if self.student_fee.is_closed:

            raise ValidationError({
                "student_fee":
                    "Fee already fully paid"
            })

        if (
            self.amount >
            self.student_fee.due_amount
        ):

            raise ValidationError({
                "amount":
                    "Payment exceeds due amount"
            })

    def save(self, *args, **kwargs):

        with transaction.atomic():

            is_new = self.pk is None

            self.full_clean()

            if (
                is_new and
                not self.receipt_number
            ):

                self.receipt_number = (

                    f"RCPT-"

                    f"{uuid.uuid4().hex[:10].upper()}"
                )

            super().save(*args, **kwargs)

            if is_new:

                student_fee = (
                    self.student_fee
                )

                type(student_fee).objects.filter(
                    pk=student_fee.pk
                ).update(

                    paid_amount=(
                        F("paid_amount") + self.amount
                    )
                )

                student_fee.refresh_from_db()

    def __str__(self):

        return (

            f"{self.student_fee.student}"

            f" paid "

            f"{self.amount}"
        )