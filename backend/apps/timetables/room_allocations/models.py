from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.timetables.timetable_entries.models import TimetableEntry
class RoomAllocation(
    SessionBaseModel,
):

    timetable_entry = models.OneToOneField(
        TimetableEntry,
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