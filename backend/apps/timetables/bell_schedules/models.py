from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
    OrderedBaseModel,
)

class BellSchedule(
    SessionBaseModel,
    OrderedBaseModel,
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

    start_date = models.DateField()

    end_date = models.DateField(
        null=True,
        blank=True,
    )

    is_default = models.BooleanField(
        default=False,
    )

    class Meta:

        db_table = "tt_bell_schedules"

        ordering = [
            "display_order",
            "name",
        ]

        unique_together = (
            (
                "school",
                "academic_session",
                "code",
            ),
        )

    def __str__(self):

        return self.name