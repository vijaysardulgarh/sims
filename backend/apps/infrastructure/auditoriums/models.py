from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.infrastructure.rooms.models import (
    Room
)


class Auditorium(
    SchoolBaseModel
):

    room = models.OneToOneField(

        Room,

        on_delete=models.CASCADE,

        related_name="auditorium"
    )

    auditorium_code = models.CharField(

        max_length=50,

        unique=True
    )

    seating_capacity = (
        models.PositiveIntegerField(
            default=0
        )
    )

    stage_available = (
        models.BooleanField(
            default=True
        )
    )

    sound_system_available = (
        models.BooleanField(
            default=True
        )
    )

    projector_available = (
        models.BooleanField(
            default=False
        )
    )

    air_conditioned = (
        models.BooleanField(
            default=False
        )
    )

    green_room_available = (
        models.BooleanField(
            default=False
        )
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "auditoriums"

        verbose_name = "Auditorium"

        verbose_name_plural = (
            "Auditoriums"
        )

        ordering = [
            "auditorium_code"
        ]

    def __str__(self):

        return self.auditorium_code