from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class SubjectConstraint(
    SessionBaseModel,
):

    subject = models.OneToOneField(
        "subjects.Subject",
        on_delete=models.CASCADE,
        related_name="subject_constraint",
    )

    periods_per_week = models.PositiveIntegerField(
        default=1,
    )

    max_periods_per_day = models.PositiveIntegerField(
        default=1,
    )

    min_periods_per_day = models.PositiveIntegerField(
        default=0,
    )

    allow_consecutive_periods = models.BooleanField(
        default=False,
    )

    required_consecutive_periods = models.PositiveIntegerField(
        default=1,
    )

    avoid_first_period = models.BooleanField(
        default=False,
    )

    avoid_last_period = models.BooleanField(
        default=False,
    )

    requires_room = models.BooleanField(
        default=False,
    )

    room_type = models.CharField(
        max_length=100,
        blank=True,
    )

    requires_resource = models.BooleanField(
        default=False,
    )

    resource_type = models.CharField(
        max_length=100,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_subject_constraints"
        )

        ordering = [
            "subject__name",
        ]

    def __str__(
        self,
    ):

        return str(
            self.subject
        )