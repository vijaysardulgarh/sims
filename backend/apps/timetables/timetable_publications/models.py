from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)
from apps.staff.profiles.models import Staff

class TimetablePublication(
    SessionBaseModel,
):

    STATUS_CHOICES = (
        ("DRAFT", "Draft"),
        ("PUBLISHED", "Published"),
        ("UNPUBLISHED", "Unpublished"),
    )

    timetable = models.ForeignKey(
        "timetables.Timetable",
        on_delete=models.CASCADE,
        related_name="publications",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DRAFT",
    )

    publication_notes = models.TextField(
        blank=True,
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    published_by = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="published_timetables",
    )

    class Meta:

        db_table = (
            "tt_timetable_publications"
        )

        ordering = [
            "-created_at",
        ]

    def __str__(
        self,
    ):

        return (
            f"{self.timetable} - "
            f"{self.status}"
        )