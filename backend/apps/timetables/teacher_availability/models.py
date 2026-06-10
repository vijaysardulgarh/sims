from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class TeacherAvailability(
    SessionBaseModel,
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

    teacher = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="teacher_availabilities",
    )

    day = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
    )

    period = models.ForeignKey(
        "period_definitions.PeriodDefinition",
        on_delete=models.CASCADE,
        related_name="teacher_availabilities",
    )

    is_available = models.BooleanField(
        default=True,
    )

    reason = models.CharField(
        max_length=255,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_teacher_availabilities"
        )

        ordering = [
            "teacher",
            "day",
            "period",
        ]

        unique_together = (
            (
                "school",
                "academic_session",
                "teacher",
                "day",
                "period",
            ),
        )

    def __str__(
        self,
    ):

        return (
            f"{self.teacher} - "
            f"{self.day} - "
            f"{self.period}"
        )