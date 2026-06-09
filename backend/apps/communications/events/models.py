from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Event(
    SchoolBaseModel
):

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    banner = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    start_time = models.TimeField(
        blank=True,
        null=True
    )

    end_time = models.TimeField(
        blank=True,
        null=True
    )

    venue = models.CharField(
        max_length=255,
        blank=True
    )

    organizer = models.CharField(
        max_length=255,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "events"

        verbose_name = "Event"

        verbose_name_plural = "Events"

        ordering = [
            "-start_date"
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "school",
                    "title"
                ],
                name="unique_event_title_per_school"
            )
        ]

        indexes = [
            models.Index(
                fields=[
                    "school",
                    "start_date"
                ]
            ),
            models.Index(
                fields=[
                    "school",
                    "is_published"
                ]
            ),
        ]

    def __str__(self):

        return self.title