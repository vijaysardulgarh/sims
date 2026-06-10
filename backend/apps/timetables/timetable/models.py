from django.db import models

from apps.core.models import (
    SessionBaseModel,
    PublishableBaseModel,
)


class Timetable(
    SessionBaseModel,
    PublishableBaseModel,
):

    name = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=20,
    )

    school_class = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="timetables",
    )

    section = models.ForeignKey(
        "academics.Section",
        on_delete=models.CASCADE,
        related_name="timetables",
        null=True,
        blank=True,
    )

    bell_schedule = models.ForeignKey(
        "bell_schedules.BellSchedule",
        on_delete=models.PROTECT,
        related_name="timetables",
    )

    effective_from = models.DateField()

    effective_to = models.DateField(
        null=True,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_timetables"
        )

        ordering = [
            "school_class",
            "section",
        ]

        unique_together = (
            (
                "school",
                "academic_session",
                "school_class",
                "section",
                "code",
            ),
        )

    def __str__(
        self,
    ):

        if self.section:

            return (
                f"{self.school_class} - "
                f"{self.section}"
            )

        return str(
            self.school_class
        )