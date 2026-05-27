from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class AcademicSession(
    SchoolBaseModel
):

    name = models.CharField(
        max_length=20
    )

    start_date = models.DateField()

    end_date = models.DateField()

    is_current = models.BooleanField(
        default=False
    )

    class Meta:

        unique_together = (
            "school",
            "name"
        )

        ordering = [
            "-start_date"
        ]

    def __str__(self):

        return (
            f"{self.name}"
        )