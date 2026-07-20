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
        verbose_name="Day",
    )

    is_working_day = models.BooleanField(
        default=True,
        help_text="Uncheck for holidays or weekly off.",
    )

    is_half_day = models.BooleanField(
        default=False,
        help_text="Check if only part of the day is working.",
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "tt_working_days"

        verbose_name = "Working Day"

        verbose_name_plural = "Working Days"

        ordering = [
            "display_order",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "school",
                    "academic_session",
                    "day_code",
                ],
                name="unique_working_day_per_session",
            ),
        ]

        indexes = [
            models.Index(
                fields=[
                    "school",
                    "academic_session",
                ],
            ),
            models.Index(
                fields=[
                    "day_code",
                ],
            ),
        ]

    def __str__(self):
        return self.get_day_code_display()