from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.examinations.exams.models import (
    Exam,
)


class GradeCalculation(
    SessionBaseModel
):

    grade = models.CharField(
        max_length=20,
    )

    minimum_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    maximum_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    grade_point = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "grade_calculations"
        )

        ordering = [
            "-minimum_percentage",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "academic_session",
                    "grade",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name="unique_grade_calculation",
            ),
        ]

    def __str__(self):

        return self.grade