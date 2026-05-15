from django.db import models
from django.core.exceptions import ValidationError


class FeeStructure(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="fee_structures"
    )

    class_obj = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="fee_structures"
    )

    stream = models.ForeignKey(
        "academics.Stream",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    session = models.CharField(
        max_length=20,
        db_index=True
    )

    admission_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    rcf = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    cwf = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    ccwf = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    other_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(
        default=True,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    @property
    def total_fee(self):

        return (
            self.admission_fee +
            self.rcf +
            self.cwf +
            self.ccwf +
            self.other_fee
        )

    def clean(self):

        fields = [
            self.admission_fee,
            self.rcf,
            self.cwf,
            self.ccwf,
            self.other_fee,
        ]

        if any(f < 0 for f in fields):
            raise ValidationError(
                "Fee values cannot be negative"
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        if self.stream:
            return (
                f"{self.class_obj} "
                f"({self.stream}) - {self.session}"
            )

        return (
            f"{self.class_obj} - {self.session}"
        )