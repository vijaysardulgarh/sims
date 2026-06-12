from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.examinations.exams.models import (
    Exam,
)

from apps.students.profiles.models import (
    Student,
)

from apps.academics.subjects.models import (
    Subject,
)


class MarkEntry(
    SessionBaseModel
):

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="mark_entries",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="mark_entries",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.PROTECT,

        related_name="mark_entries",
    )

    theory_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    practical_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    oral_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    project_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    is_absent = models.BooleanField(
        default=False,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "mark_entries"

        ordering = [
            "student",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "exam",
                    "student",
                    "subject",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name="unique_mark_entry",
            ),
        ]

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.subject}"
        )