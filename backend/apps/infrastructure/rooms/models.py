from django.db import models

from django.core.exceptions import (
    ValidationError
)

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

    # =====================================
    # VALIDATION
    # =====================================

    def clean(self):

        if (

            self.floor

            and

            self.building

            and

            self.floor.building_id
            !=
            self.building_id

        ):

            raise ValidationError(

                "Selected floor does not belong to the selected building."
            )

        if (

            self.floor

            and

            self.school

            and

            self.floor.school_id
            !=
            self.school_id

        ):

            raise ValidationError(

                "Floor must belong to the same school."
            )

        if (

            self.building

            and

            self.school

            and

            self.building.school_id
            !=
            self.school_id

        ):

            raise ValidationError(

                "Building must belong to the same school."
            )

        if (

            self.area is not None

            and

            self.area <= 0

        ):

            raise ValidationError(

                "Area must be greater than zero."
            )

        if (

            self.capacity is not None

            and

            self.capacity <= 0

        ):

            raise ValidationError(

                "Capacity must be greater than zero."
            )

    class Meta:

        db_table = "rooms"

        verbose_name = "Room"

        verbose_name_plural = "Rooms"

        ordering = [

            "building",

            "floor",

            "room_number"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[

                    "building",

                    "room_number"
                ],

                name=(
                    "unique_room_number_per_building"
                )
            ),

            models.UniqueConstraint(

                fields=[

                    "building",

                    "room_name"
                ],

                name=(
                    "unique_room_name_per_building"
                )
            ),
        ]

        indexes = [

            models.Index(
                fields=[
                    "school"
                ]
            ),

            models.Index(
                fields=[
                    "building"
                ]
            ),

            models.Index(
                fields=[
                    "floor"
                ]
            ),

            models.Index(
                fields=[
                    "room_type"
                ]
            ),

            models.Index(
                fields=[
                    "room_number"
                ]
            ),

            models.Index(
                fields=[
                    "is_active"
                ]
            ),

            models.Index(
                fields=[
                    "is_deleted"
                ]
            ),
        ]

    def __str__(self):

        return (

            f"{self.room_number}"

            f" - "

            f"{self.room_name}"
        )