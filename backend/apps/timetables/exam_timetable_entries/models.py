from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.staff.profiles.models import (
    Staff,
)
from apps.academics.subjects.models import Subject
from apps.examinations.exams.models import Exam
from apps.timetables.exam_timetables.models import ExamTimetable
class ExamTimetableEntry(
    SessionBaseModel,
):

    exam_timetable = models.ForeignKey(
        ExamTimetable,
        on_delete=models.CASCADE,
        related_name="entries",
    )

    examination = models.ForeignKey(
        Exam,
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
        Subject,
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
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="exam_timetable_invigilations",
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