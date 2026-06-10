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


class Library(
    SchoolBaseModel
):

    room = models.OneToOneField(

        Room,

        on_delete=models.CASCADE,

        related_name="library"
    )

    library_code = models.CharField(
        max_length=50
    )

    librarian = models.ForeignKey(

        Staff,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="managed_libraries"
    )

    seating_capacity = models.PositiveIntegerField(
        default=0
    )

    total_books = models.PositiveIntegerField(
        default=0
    )

    digital_library = models.BooleanField(
        default=False
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
            != "LIBRARY"
        ):

            raise ValidationError(
                "Selected room is not a library room."
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
            self.librarian
            and self.school
            and self.librarian.school_id
            != self.school_id
        ):

            raise ValidationError(
                "Librarian must belong to the same school."
            )

    class Meta:

        db_table = "libraries"

        verbose_name = "Library"

        verbose_name_plural = (
            "Libraries"
        )

        ordering = [
            "library_code"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "library_code"
                ],

                name=(
                    "unique_school_library_code"
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
                    "library_code"
                ]
            ),

            models.Index(
                fields=[
                    "room"
                ]
            ),

            models.Index(
                fields=[
                    "librarian"
                ]
            ),
        ]

    def __str__(self):

        return (
            f"{self.library_code}"
        )