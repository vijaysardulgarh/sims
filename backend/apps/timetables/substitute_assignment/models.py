from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class SubstituteAssignment(
    SessionBaseModel,
):

    timetable_entry = models.ForeignKey(
        "timetable_entries.TimetableEntry",
        on_delete=models.CASCADE,
        related_name="substitute_assignments",
    )

    original_teacher = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="original_substitutions",
    )

    substitute_teacher = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="assigned_substitutions",
    )

    substitution_date = models.DateField()

    reason = models.TextField(
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_substitute_assignments"
        )

        ordering = [
            "-substitution_date",
        ]

        unique_together = (
            (
                "timetable_entry",
                "substitution_date",
            ),
        )

    def __str__(
        self,
    ):

        return (
            f"{self.original_teacher} → "
            f"{self.substitute_teacher}"
        )