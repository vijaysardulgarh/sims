from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)
from apps.staff.profiles.models import (
    Staff,
)
from apps.academics.subjects.models import Subject
from apps.timetables.period_definitions.models import PeriodDefinition

from apps.timetables.timetables.models import (
    Timetable,
)

from apps.infrastructure.rooms.models import (
    Room
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
        Timetable,
        on_delete=models.CASCADE,
        related_name="entries",
    )

    day = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
    )

    period = models.ForeignKey(
        PeriodDefinition,
        on_delete=models.PROTECT,
        related_name="timetable_entries",
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name="timetable_entries",
        null=True,
        blank=True,
    )

    teacher = models.ForeignKey(
        Staff,
        on_delete=models.PROTECT,
        related_name="timetable_entries",
        null=True,
        blank=True,
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name="timetable_entries",
        null=True,
        blank=True,
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