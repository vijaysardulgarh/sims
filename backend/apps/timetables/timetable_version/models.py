from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class TimetableVersion(
    SessionBaseModel,
):

    timetable = models.ForeignKey(
        "timetables.Timetable",
        on_delete=models.CASCADE,
        related_name="versions",
    )

    version_number = models.PositiveIntegerField()

    version_name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    snapshot_data = models.JSONField(
        default=dict,
        blank=True,
    )

    is_current = models.BooleanField(
        default=False,
    )

    class Meta:

        db_table = (
            "tt_timetable_versions"
        )

        ordering = [
            "-version_number",
        ]

        unique_together = (
            (
                "timetable",
                "version_number",
            ),
        )

    def __str__(
        self,
    ):

        return (
            f"{self.timetable} "
            f"V{self.version_number}"
        )