from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class RoomAllocation(
    SessionBaseModel,
):

    timetable_entry = models.OneToOneField(
        "timetable_entries.TimetableEntry",
        on_delete=models.CASCADE,
        related_name="room_allocation",
    )

    room = models.ForeignKey(
        "infrastructure.Room",
        on_delete=models.CASCADE,
        related_name="room_allocations",
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "tt_room_allocations"

        ordering = [
            "-created_at",
        ]

    def __str__(
        self,
    ):

        return (
            f"{self.room}"
        )