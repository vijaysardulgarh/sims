from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.staff.profiles.models import (
    Staff,
)
from apps.timetables.timetable_entries.models import TimetableEntry

class TimetableConflict(
    SessionBaseModel,
):

    CONFLICT_TYPES = (
        (
            "TEACHER_CONFLICT",
            "Teacher Conflict",
        ),
        (
            "ROOM_CONFLICT",
            "Room Conflict",
        ),
        (
            "RESOURCE_CONFLICT",
            "Resource Conflict",
        ),
        (
            "WORKLOAD_CONFLICT",
            "Workload Conflict",
        ),
        (
            "AVAILABILITY_CONFLICT",
            "Availability Conflict",
        ),
        (
            "SUBJECT_CONSTRAINT",
            "Subject Constraint",
        ),
        (
            "SUBJECT_REQUIREMENT",
            "Subject Requirement",
        ),
        (
            "TIMING_CONFLICT",
            "Timing Conflict",
        ),
        (
            "OTHER",
            "Other",
        ),
    )

    timetable = models.ForeignKey(
        "timetables.Timetable",
        on_delete=models.CASCADE,
        related_name="conflicts",
    )

    timetable_entry = models.ForeignKey(
        TimetableEntry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="conflicts",
    )

    conflict_type = models.CharField(
        max_length=50,
        choices=CONFLICT_TYPES,
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField()

    is_resolved = models.BooleanField(
        default=False,
    )

    resolved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    resolved_by = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="resolved_timetable_conflicts",
    )

    class Meta:

        db_table = (
            "tt_timetable_conflicts"
        )

        ordering = [
            "-created_at",
        ]

    def __str__(
        self,
    ):

        return (
            f"{self.conflict_type} - "
            f"{self.title}"
        )