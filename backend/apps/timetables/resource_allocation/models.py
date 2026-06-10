from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class ResourceAllocation(
    SessionBaseModel,
):

    timetable_entry = models.ForeignKey(
        "timetable_entries.TimetableEntry",
        on_delete=models.CASCADE,
        related_name="resource_allocations",
    )

    resource = models.ForeignKey(
        "infrastructure.Resource",
        on_delete=models.CASCADE,
        related_name="resource_allocations",
    )

    allocated_from = models.DateField(
        null=True,
        blank=True,
    )

    allocated_to = models.DateField(
        null=True,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "tt_resource_allocations"

        ordering = [
            "-created_at",
        ]

        unique_together = (
            (
                "timetable_entry",
                "resource",
            ),
        )

    def __str__(self):

        return (
            f"{self.resource}"
        )