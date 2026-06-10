from django.db import models

from apps.core.models.base_models import (
    SessionBaseModel,
)

from apps.exams.exam_types.models import (
    ExamType,
)


class Exam(
    SessionBaseModel
):

    exam_type = models.ForeignKey(

        ExamType,

        on_delete=models.PROTECT,

        related_name="exams",
    )

    name = models.CharField(
        max_length=255,
    )

    start_date = models.DateField()

    end_date = models.DateField()

    result_publish_date = models.DateField(

        null=True,

        blank=True,
    )

    is_marks_locked = models.BooleanField(
        default=False,
    )

    is_result_published = models.BooleanField(
        default=False,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "exams"

        ordering = [
            "-start_date",
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

                name="unique_exam_name",
            ),
        ]

    def __str__(self):

        return self.name