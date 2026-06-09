from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel
)

from apps.associations.associations.models import (
    Association
)

from apps.documents.models import (
    Document
)


# =============================================================================
# MEETING TYPES
# =============================================================================

TYPE_PHYSICAL = "PHYSICAL"
TYPE_ONLINE = "ONLINE"
TYPE_HYBRID = "HYBRID"

TYPE_CHOICES = [

    (TYPE_PHYSICAL, "Physical"),

    (TYPE_ONLINE, "Online"),

    (TYPE_HYBRID, "Hybrid"),

]


# =============================================================================
# MEETING STATUS
# =============================================================================

STATUS_SCHEDULED = "SCHEDULED"
STATUS_COMPLETED = "COMPLETED"
STATUS_CANCELLED = "CANCELLED"
STATUS_POSTPONED = "POSTPONED"

STATUS_CHOICES = [

    (STATUS_SCHEDULED, "Scheduled"),

    (STATUS_COMPLETED, "Completed"),

    (STATUS_CANCELLED, "Cancelled"),

    (STATUS_POSTPONED, "Postponed"),

]


class AssociationMeeting(
    SessionBaseModel
):

    association = models.ForeignKey(
        Association,
        on_delete=models.CASCADE,
        related_name="meetings"
    )

    title = models.CharField(
        max_length=255
    )

    meeting_date = models.DateTimeField(
        db_index=True
    )

    meeting_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default=TYPE_PHYSICAL
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_SCHEDULED
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    agenda = models.TextField(
        blank=True
    )

    conducted_by = models.ForeignKey(
        "staff.Staff",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    minutes_document = models.ForeignKey(
        Document,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )