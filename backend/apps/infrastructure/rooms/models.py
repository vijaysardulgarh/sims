from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.infrastructure.buildings.models import (
    Building
)

from apps.infrastructure.floors.models import (
    Floor
)


class Room(
    SchoolBaseModel
):

    ROOM_TYPE_CHOICES = [

        ("CLASSROOM", "Classroom"),

        ("LABORATORY", "Laboratory"),

        ("LIBRARY", "Library"),

        ("OFFICE", "Office"),

        ("STAFF_ROOM", "Staff Room"),

        ("STORE", "Store Room"),

        ("AUDITORIUM", "Auditorium"),

        ("OTHER", "Other"),
    ]

    building = models.ForeignKey(

        Building,

        on_delete=models.CASCADE,

        related_name="rooms"
    )

    floor = models.ForeignKey(

        Floor,

        on_delete=models.CASCADE,

        related_name="rooms"
    )

    room_number = models.CharField(
        max_length=50
    )

    room_name = models.CharField(
        max_length=255
    )

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPE_CHOICES
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    capacity = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    class Meta:

        db_table = "rooms"

        ordering = [
            "building",
            "floor",
            "room_number"
        ]

    def __str__(self):

        return (
            f"{self.room_number} - "
            f"{self.room_name}"
        )