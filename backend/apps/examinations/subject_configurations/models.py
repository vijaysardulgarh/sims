from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.examinations.exams.models import (
    Exam,
)

from apps.academics.subjects.models import (
    Subject,
)


class SubjectConfiguration(
    SessionBaseModel
):

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="subject_configurations",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.PROTECT,

        related_name="subject_configurations",
    )

    maximum_marks = models.DecimalField(

        max_digits=6,

        decimal_places=2,
    )

    passing_marks = models.DecimalField(

        max_digits=6,

        decimal_places=2,
    )

    theory_marks = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        default=0,
    )

    practical_marks = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        default=0,
    )

    internal_marks = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        default=0,
    )

    oral_marks = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        default=0,
    )

    project_marks = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        default=0,
    )

    is_theory_enabled = models.BooleanField(
        default=True,
    )

    is_practical_enabled = models.BooleanField(
        default=False,
    )

    is_internal_enabled = models.BooleanField(
        default=False,
    )

    is_oral_enabled = models.BooleanField(
        default=False,
    )

    is_project_enabled = models.BooleanField(
        default=False,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "subject_configurations"
        )

        ordering = [
            "subject",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "exam",
                    "subject",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name=(
                    "unique_exam_subject_configuration"
                ),
            ),
        ]

    def __str__(self):

        return (
            f"{self.exam} - "
            f"{self.subject}"
        )