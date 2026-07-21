from django.core.exceptions import ValidationError
from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)
from apps.timetables.subject_requirements.models import (
    SubjectRequirement,
)


class SubjectConstraint(
    SessionBaseModel,
):

    TIME_SLOT_CHOICES = [

        ("ANY", "Any"),

        ("MORNING", "Morning"),

        ("AFTERNOON", "Afternoon"),

    ]

    subject_requirement = models.OneToOneField(
        SubjectRequirement,
        on_delete=models.CASCADE,
        related_name="subject_constraint",
    )

    priority = models.PositiveSmallIntegerField(
        default=5,
        help_text="Lower value indicates higher scheduling priority.",
    )

    max_periods_per_day = models.PositiveSmallIntegerField(
        default=1,
    )

    allow_consecutive_periods = models.BooleanField(
        default=False,
    )

    required_consecutive_periods = models.PositiveSmallIntegerField(
        default=1,
    )

    spread_across_week = models.BooleanField(
        default=True,
    )

    avoid_first_period = models.BooleanField(
        default=False,
    )

    avoid_last_period = models.BooleanField(
        default=False,
    )

    preferred_time_slot = models.CharField(
        max_length=10,
        choices=TIME_SLOT_CHOICES,
        default="ANY",
    )

    remarks = models.TextField(
        blank=True,
    )

    def clean(self):

        super().clean()

        if (
            self.required_consecutive_periods > 1
            and not self.allow_consecutive_periods
        ):

            raise ValidationError(
                {
                    "required_consecutive_periods":
                    "Required consecutive periods greater than 1 require 'Allow Consecutive Periods' to be enabled."
                }
            )

    class Meta:

        db_table = (
            "tt_subject_constraints"
        )

        verbose_name = (
            "Subject Constraint"
        )

        verbose_name_plural = (
            "Subject Constraints"
        )

        ordering = [

            "subject_requirement__school_class__display_order",

            "subject_requirement__subject__name",

        ]

    def save(
        self,
        *args,
        **kwargs,
    ):

        self.full_clean()

        super().save(
            *args,
            **kwargs,
        )

    def __str__(self):

        return (
            f"{self.subject_requirement.school_class} - "
            f"{self.subject_requirement.subject}"
        )