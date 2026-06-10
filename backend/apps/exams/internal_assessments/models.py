from django.db import models

from apps.core.models.base_models import (
    SessionBaseModel,
)

from apps.exams.exams.models import (
    Exam,
)

from apps.students.students.models import (
    Student,
)

from apps.academics.subjects.models import (
    Subject,
)


class InternalAssessment(
    SessionBaseModel
):

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="internal_assessments",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="internal_assessments",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.PROTECT,

        related_name="internal_assessments",
    )

    assignment_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    project_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    notebook_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    attendance_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    total_marks = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        default=0,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "internal_assessments"
        )

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

                name=(
                    "unique_internal_assessment"
                ),
            ),
        ]

    def save(
        self,
        *args,
        **kwargs
    ):

        self.total_marks = (

            self.assignment_marks

            + self.project_marks

            + self.notebook_marks

            + self.attendance_marks
        )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.subject}"
        )