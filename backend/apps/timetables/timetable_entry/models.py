from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class TimetableEntry(
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

    timetable = models.ForeignKey(
        "timetables.Timetable",
        on_delete=models.CASCADE,
        related_name="entries",
    )

    day = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
    )

    period = models.ForeignKey(
        "period_definitions.PeriodDefinition",
        on_delete=models.PROTECT,
        related_name="timetable_entries",
    )

    subject = models.ForeignKey(
        "subjects.Subject",
        on_delete=models.PROTECT,
        related_name="timetable_entries",
    )

    teacher = models.ForeignKey(
        "employees.Employee",
        on_delete=models.PROTECT,
        related_name="timetable_entries",
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_timetable_entries"
        )

        ordering = [
            "day",
            "period",
        ]

        unique_together = (
            (
                "timetable",
                "day",
                "period",
            ),
        )

    def __str__(
        self,
    ):

        return (
            f"{self.day} - "
            f"{self.period} - "
            f"{self.subject}"
        )