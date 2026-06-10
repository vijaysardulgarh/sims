from django.db import models

from apps.core.models.base_models import (
    SessionBaseModel,
)

from apps.exams.exams.models import (
    Exam,
)


class ResultPublication(
    SessionBaseModel
):

    exam = models.OneToOneField(

        Exam,

        on_delete=models.CASCADE,

        related_name="result_publication",
    )

    publication_date = models.DateTimeField()

    is_published = models.BooleanField(
        default=False,
    )

    published_at = models.DateTimeField(

        null=True,

        blank=True,
    )

    published_by = models.ForeignKey(

        "users.User",

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="published_results",
    )

    notification_sent = models.BooleanField(
        default=False,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "result_publications"
        )

        ordering = [
            "-publication_date",
        ]

    def __str__(self):

        return (
            f"{self.exam}"
        )