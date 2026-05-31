from django.db import models

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

        max_length=50,

        unique=True
    )

    incharge = models.ForeignKey(

        Staff,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="laboratories"
    )

    equipment_count = (
        models.PositiveIntegerField(
            default=0
        )
    )

    safety_equipment_available = (
        models.BooleanField(
            default=True
        )
    )

    internet_enabled = (
        models.BooleanField(
            default=False
        )
    )

    is_active = models.BooleanField(
        default=True
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

    def __str__(self):

        return (
            f"{self.lab_code}"
        )