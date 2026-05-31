from django.db import models

from django.db.models import (
    Q
)

from django.core.exceptions import (
    ValidationError
)

from apps.academics.classes.models import Class
from apps.academics.streams.models import Stream
from apps.core.common.base.models import SchoolBaseModel

class FeeStructure(SchoolBaseModel):

    class_obj = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="fee_structures",
        db_index=True
    )

    stream = models.ForeignKey(
        Stream,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="fee_structures",
        db_index=True
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
                fields=["is_active"]
            ),
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "class_obj",
                    "stream",
                    "session"
                ],
                name=(
                    "unique_fee_structure_"
                    "per_class_stream_session"
                )
            ),

            models.CheckConstraint(
                condition=Q(admission_fee__gte=0),
                name="admission_fee_positive"
            ),

            models.CheckConstraint(
                condition=Q(rcf__gte=0),
                name="rcf_positive"
            ),

            models.CheckConstraint(
                condition=Q(cwf__gte=0),
                name="cwf_positive"
            ),

            models.CheckConstraint(
                condition=Q(ccwf__gte=0),
                name="ccwf_positive"
            ),

            models.CheckConstraint(
                condition=Q(other_fee__gte=0),
                name="other_fee_positive"
            ),
        ]

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

            raise ValidationError({
                "fee":
                    (
                        "Fee values cannot "
                        "be negative"
                    )
            })

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        if self.stream:

            return (

                f"{self.class_obj} "

                f"({self.stream}) "

                f"- {self.session}"
            )

        return (
            f"{self.class_obj} "
            f"- {self.session}"
        )