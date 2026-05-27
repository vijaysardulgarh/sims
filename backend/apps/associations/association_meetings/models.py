# =============================================================================
# associations/models/association_meeting.py
# =============================================================================

from django.db import models

from apps.documents.models import Document
from apps.associations.associations.models import (
    Association
)
from apps.core.common.base.models import SessionBaseModel


class AssociationMeeting(SessionBaseModel):

    association = models.ForeignKey(
        Association,
        on_delete=models.CASCADE,
        related_name="meetings",
        db_index=True
    )

    meeting_date = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True
    )

    agenda = models.TextField(blank=True)

    location = models.CharField(max_length=100)

    minutes_document = models.ForeignKey(
        Document,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Association Meeting"
        verbose_name_plural = "Association Meetings"

        ordering = ["-meeting_date"]

        indexes = [

            models.Index(
                fields=[
                    "school",
                    "academic_session",
                    "meeting_date"
                ]
            ),
        ]

    def __str__(self):

        return (
            f"{self.association.name} "
            f"Meeting on {self.meeting_date}"
        )