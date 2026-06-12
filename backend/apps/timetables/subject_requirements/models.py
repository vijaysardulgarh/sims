from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)
from apps.academics.subjects.models import Subject

class SubjectRequirement(
    SessionBaseModel,
):

    school_class = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="subject_requirements",
    )

    section = models.ForeignKey(
        "academics.Section",
        on_delete=models.CASCADE,
        related_name="subject_requirements",
        null=True,
        blank=True,
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="subject_requirements",
    )

    periods_per_week = models.PositiveIntegerField(
        default=1,
    )

    periods_per_day = models.PositiveIntegerField(
        default=1,
    )

    practical_periods_per_week = models.PositiveIntegerField(
        default=0,
    )

    is_mandatory = models.BooleanField(
        default=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_subject_requirements"
        )

        ordering = [
            "school_class",
            "subject",
        ]

        unique_together = (
            (
                "school",
                "academic_session",
                "school_class",
                "section",
                "subject",
            ),
        )

    def __str__(
        self,
    ):

        return (
            f"{self.school_class} - "
            f"{self.subject}"
        )