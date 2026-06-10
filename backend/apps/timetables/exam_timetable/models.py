from django.db import models

from apps.core.models import (
    SessionBaseModel,
    PublishableBaseModel,
)


class ExamTimetable(
    SessionBaseModel,
    PublishableBaseModel,
):

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    examination = models.ForeignKey(
        "examinations.Examination",
        on_delete=models.CASCADE,
        related_name="exam_timetables",
    )

    description = models.TextField(
        blank=True,
    )

    start_date = models.DateField()

    end_date = models.DateField()

    class Meta:

        db_table = "exam_timetables"

        ordering = [
            "-start_date",
            "name",
        ]

        unique_together = (
            (
                "school",
                "academic_session",
                "code",
            ),
        )

    def __str__(self):

        return self.name