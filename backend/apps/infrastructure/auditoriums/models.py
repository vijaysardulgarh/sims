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
        max_length=50
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

    class Meta:

        db_table = "auditoriums"

        verbose_name = "Auditorium"

        verbose_name_plural = (
            "Auditoriums"
        )

        ordering = [
            "auditorium_code"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "auditorium_code"
                ],

                name=(
                    "unique_school_auditorium_code"
                )
            )
        ]

        indexes = [

            models.Index(
                fields=[
                    "auditorium_code"
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
            f"{self.auditorium_code}"
        )