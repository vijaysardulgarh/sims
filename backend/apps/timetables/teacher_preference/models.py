from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class TeacherPreference(
    SessionBaseModel,
):

    teacher = models.OneToOneField(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="teacher_preference",
    )

    prefer_first_period = models.BooleanField(
        default=False,
    )

    avoid_first_period = models.BooleanField(
        default=False,
    )

    prefer_last_period = models.BooleanField(
        default=False,
    )

    avoid_last_period = models.BooleanField(
        default=False,
    )

    prefer_consecutive_periods = models.BooleanField(
        default=False,
    )

    avoid_gaps_between_classes = models.BooleanField(
        default=False,
    )

    max_periods_per_day = models.PositiveIntegerField(
        default=6,
    )

    max_periods_per_week = models.PositiveIntegerField(
        default=36,
    )

    preferred_free_day = models.CharField(
        max_length=3,
        choices=(
            ("MON", "Monday"),
            ("TUE", "Tuesday"),
            ("WED", "Wednesday"),
            ("THU", "Thursday"),
            ("FRI", "Friday"),
            ("SAT", "Saturday"),
            ("SUN", "Sunday"),
        ),
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_teacher_preferences"
        )

        ordering = [
            "teacher",
        ]

    def __str__(
        self,
    ):

        return str(
            self.teacher
        )