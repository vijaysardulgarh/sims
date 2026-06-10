from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class ExamTimetableEntry(
    SessionBaseModel,
):

    exam_timetable = models.ForeignKey(
        "exam_timetables.ExamTimetable",
        on_delete=models.CASCADE,
        related_name="entries",
    )

    examination = models.ForeignKey(
        "examinations.Examination",
        on_delete=models.CASCADE,
        related_name="timetable_entries",
    )

    school_class = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="exam_timetable_entries",
    )

    section = models.ForeignKey(
        "academics.Section",
        on_delete=models.CASCADE,
        related_name="exam_timetable_entries",
        null=True,
        blank=True,
    )

    subject = models.ForeignKey(
        "subjects.Subject",
        on_delete=models.CASCADE,
        related_name="exam_timetable_entries",
    )

    exam_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    duration_minutes = models.PositiveIntegerField(
        default=180,
    )

    maximum_marks = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=100,
    )

    passing_marks = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=33,
    )

    room = models.ForeignKey(
        "infrastructure.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="exam_timetable_entries",
    )

    invigilator = models.ForeignKey(
        "employees.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="invigilated_exams",
    )

    instructions = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "exam_timetable_entries"

        ordering = [
            "exam_date",
            "start_time",
        ]

        unique_together = (
            (
                "exam_timetable",
                "school_class",
                "section",
                "subject",
            ),
        )

    def __str__(
        self,
    ):

        return (
            f"{self.subject} - "
            f"{self.exam_date}"
        )