from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.infrastructure.rooms.models import (
    Room
)

from apps.staff.staffs.models import (
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

        max_length=50,

        unique=True
    )

    librarian = models.ForeignKey(

        Staff,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="managed_libraries"
    )

    seating_capacity = (
        models.PositiveIntegerField(
            default=0
        )
    )

    total_books = (
        models.PositiveIntegerField(
            default=0
        )
    )

    digital_library = (
        models.BooleanField(
            default=False
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

        db_table = "libraries"

        verbose_name = "Library"

        verbose_name_plural = (
            "Libraries"
        )

        ordering = [
            "library_code"
        ]

    def __str__(self):

        return self.library_code