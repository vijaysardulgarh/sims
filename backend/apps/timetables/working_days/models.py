from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
    OrderedBaseModel,
)


class WorkingDay(
    SessionBaseModel,
    OrderedBaseModel,
):

    DAY_CHOICES = (
        ("MON", "Monday"),
        ("TUE", "Tuesday"),
        ("WED", "Wednesday"),
        ("THU", "Thursday"),
        ("FRI", "Friday"),
        ("SAT", "Saturday"),
        ("SUN", "Sunday"),
    )

    day_code = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
    )

    is_working_day = models.BooleanField(
        default=True,
    )

    is_half_day = models.BooleanField(
        default=False,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_working_days"
        )

        ordering = [
            "display_order",
        ]

        unique_together = (
            (
                "school",
                "academic_session",
                "day_code",
            ),
        )

    def __str__(
        self,
    ):

        return self.get_day_code_display()