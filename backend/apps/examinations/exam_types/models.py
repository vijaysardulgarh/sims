from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
    OrderedBaseModel,
)


class ExamType(
    SessionBaseModel,
    OrderedBaseModel
):

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    description = models.TextField(
        blank=True,
    )

    color = models.CharField(
        max_length=20,
        blank=True,
    )

    weightage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    allow_practical = models.BooleanField(
        default=False,
    )

    allow_internal_assessment = models.BooleanField(
        default=False,
    )

    class Meta:

        db_table = "exam_types"

        ordering = [
            "display_order",
            "name",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "academic_session",
                    "name",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name="unique_exam_type_name",
            ),

            models.UniqueConstraint(

                fields=[
                    "school",
                    "academic_session",
                    "code",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name="unique_exam_type_code",
            ),
        ]

    def __str__(self):

        return self.name