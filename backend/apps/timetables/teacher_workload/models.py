from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class TeacherWorkload(
    SessionBaseModel,
):

    teacher = models.OneToOneField(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="teacher_workload",
    )

    max_periods_per_day = models.PositiveIntegerField(
        default=6,
    )

    min_periods_per_day = models.PositiveIntegerField(
        default=0,
    )

    max_periods_per_week = models.PositiveIntegerField(
        default=36,
    )

    min_periods_per_week = models.PositiveIntegerField(
        default=0,
    )

    max_consecutive_periods = models.PositiveIntegerField(
        default=3,
    )

    allow_overtime = models.BooleanField(
        default=False,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_teacher_workloads"
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