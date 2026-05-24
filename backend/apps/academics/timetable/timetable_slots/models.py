from django.db import models

from django.core.exceptions import (
    ValidationError
)

from django.db.models import Q

from apps.academics.timetable.days.models import Day
from apps.core.common.base.models import SchoolBaseModel

class TimetableSlot( SchoolBaseModel):


    day = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        related_name="slots",
        db_index=True
    )

    sequence_number = (
        models.PositiveIntegerField()
    )

    period_number = (
        models.PositiveIntegerField(
            null=True,
            blank=True
        )
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    is_break = models.BooleanField(
        default=False
    )

    is_assembly = models.BooleanField(
        default=False
    )

    is_special_event = models.BooleanField(
        default=False
    )

    title = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:

        ordering = [
            "day__sequence",
            "sequence_number"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "day",
                    "sequence_number"
                ],
                name="unique_slot_sequence_per_day"
            ),

            models.UniqueConstraint(
                fields=[
                    "school",
                    "day",
                    "period_number"
                ],

                condition=Q(
                    period_number__isnull=False
                ),

                name="unique_period_per_day"
            )
        ]

    def clean(self):

        if (
            self.start_time >=
            self.end_time
        ):

            raise ValidationError(
                "End time must be "
                "greater than start time."
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        if self.period_number:

            return (
                f"{self.day.name}"
                f" - "
                f"Period "
                f"{self.period_number}"
            )

        return (
            f"{self.day.name}"
            f" - Special Slot"
        )