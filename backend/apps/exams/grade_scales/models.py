from django.db import models

from apps.core.models.base_models import (
    SessionBaseModel,
)


class GradeScale(
    SessionBaseModel
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

    is_default = models.BooleanField(
        default=False,
    )

    class Meta:

        db_table = "grade_scales"

        ordering = [
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

                name="unique_grade_scale_name",
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

                name="unique_grade_scale_code",
            ),
        ]

    def __str__(self):

        return self.name