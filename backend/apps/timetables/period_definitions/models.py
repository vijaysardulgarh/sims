from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
    OrderedBaseModel,
)
from apps.timetables.bell_schedules.models import BellSchedule

class PeriodDefinition(
    SessionBaseModel,
    OrderedBaseModel,
):

    bell_schedule = models.ForeignKey(
        BellSchedule,
        on_delete=models.CASCADE,
        related_name="period_definitions",
    )

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    is_instructional = models.BooleanField(
        default=True,
    )

    is_break = models.BooleanField(
        default=False,
    )

    is_lunch = models.BooleanField(
        default=False,
    )

    is_assembly = models.BooleanField(
        default=False,
    )

    is_zero_period = models.BooleanField(
        default=False,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "tt_period_definitions"

        ordering = [
            "display_order",
            "start_time",
        ]

        unique_together = (
            (
                "school",
                "academic_session",
                "bell_schedule",
                "code",
            ),
        )

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.start_time}-{self.end_time})"
        )