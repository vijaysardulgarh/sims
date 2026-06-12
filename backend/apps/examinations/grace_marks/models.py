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


class GraceMark(
    SessionBaseModel
):

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="grace_marks",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="grace_marks",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.CASCADE,

        related_name="grace_marks",
    )

    original_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,
    )

    grace_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    final_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,
    )

    reason = models.TextField()

    approved = models.BooleanField(
        default=False,
    )

    approved_at = models.DateTimeField(

        null=True,

        blank=True,
    )

    class Meta:

        db_table = "grace_marks"

        ordering = [
            "-created_at",
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

                name="unique_grace_mark_record",
            ),
        ]

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.subject}"
        )