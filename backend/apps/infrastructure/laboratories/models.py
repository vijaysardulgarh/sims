from django.db import models
from django.core.exceptions import ValidationError

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.infrastructure.rooms.models import (
    Room
)

from apps.staff.profiles.models import (
    Staff
)


class Laboratory(
    SchoolBaseModel
):

    LAB_TYPE_CHOICES = [

        ("PHYSICS", "Physics"),

        ("CHEMISTRY", "Chemistry"),

        ("BIOLOGY", "Biology"),

        ("COMPUTER", "Computer"),

        ("MATHEMATICS", "Mathematics"),

        ("LANGUAGE", "Language"),

        ("ROBOTICS", "Robotics"),

        ("OTHER", "Other"),
    ]

    room = models.OneToOneField(

        Room,

        on_delete=models.CASCADE,

        related_name="laboratory"
    )

    lab_type = models.CharField(

        max_length=20,

        choices=LAB_TYPE_CHOICES
    )

    lab_code = models.CharField(
        max_length=50
    )

    incharge = models.ForeignKey(

        Staff,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="laboratories"
    )

    equipment_count = models.PositiveIntegerField(
        default=0
    )

    safety_equipment_available = models.BooleanField(
        default=True
    )

    internet_enabled = models.BooleanField(
        default=False
    )

    def clean(self):

        if (
            self.room
            and hasattr(
                self.room,
                "room_type"
            )
            and self.room.room_type
            != "LABORATORY"
        ):

            raise ValidationError(
                "Selected room is not a laboratory room."
            )

        if (
            self.room
            and self.school
            and self.room.school_id
            != self.school_id
        ):

            raise ValidationError(
                "Room must belong to the same school."
            )

        if (
            self.incharge
            and self.school
            and self.incharge.school_id
            != self.school_id
        ):

            raise ValidationError(
                "Laboratory incharge must belong to the same school."
            )

    class Meta:

        db_table = "laboratories"

        verbose_name = "Laboratory"

        verbose_name_plural = (
            "Laboratories"
        )

        ordering = [
            "lab_code"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "lab_code"
                ],

                name=(
                    "unique_school_lab_code"
                )
            )
        ]

        indexes = [

            models.Index(
                fields=[
                    "school"
                ]
            ),

            models.Index(
                fields=[
                    "lab_code"
                ]
            ),

            models.Index(
                fields=[
                    "lab_type"
                ]
            ),

            models.Index(
                fields=[
                    "room"
                ]
            ),
        ]

    def __str__(self):

        return (
            f"{self.lab_code}"
        )