from django.core.exceptions import ValidationError
from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)
from apps.staff.profiles.models import (
    Staff,
)


class TeacherWorkload(
    SessionBaseModel,
):

    teacher = models.OneToOneField(
        Staff,
        on_delete=models.CASCADE,
        related_name="teacher_workload",
    )

    max_periods_per_day = models.PositiveSmallIntegerField(
        default=6,
        help_text="Maximum teaching periods allowed per day.",
    )

    min_periods_per_day = models.PositiveSmallIntegerField(
        default=0,
        help_text="Minimum teaching periods expected per day.",
    )

    max_periods_per_week = models.PositiveSmallIntegerField(
        default=36,
        help_text="Maximum teaching periods allowed per week.",
    )

    min_periods_per_week = models.PositiveSmallIntegerField(
        default=0,
        help_text="Minimum teaching periods expected per week.",
    )

    max_consecutive_periods = models.PositiveSmallIntegerField(
        default=3,
        help_text="Maximum consecutive teaching periods without a break.",
    )

    class Meta:

        db_table = "tt_teacher_workloads"

        verbose_name = "Teacher Workload"

        verbose_name_plural = "Teacher Workloads"

        ordering = [
            "teacher__name",
        ]

    def clean(self):

        if self.min_periods_per_day > self.max_periods_per_day:
            raise ValidationError(
                {
                    "min_periods_per_day":
                        "Minimum periods per day cannot exceed maximum periods per day."
                }
            )

        if self.min_periods_per_week > self.max_periods_per_week:
            raise ValidationError(
                {
                    "min_periods_per_week":
                        "Minimum periods per week cannot exceed maximum periods per week."
                }
            )

        if self.max_consecutive_periods > self.max_periods_per_day:
            raise ValidationError(
                {
                    "max_consecutive_periods":
                        "Maximum consecutive periods cannot exceed maximum periods per day."
                }
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.teacher.name} "
            f"(Max {self.max_periods_per_week}/Week)"
        )