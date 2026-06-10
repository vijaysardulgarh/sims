from django.db import models

from apps.core.models.base_models import (
    SessionBaseModel,
)

from apps.exams.mark_entries.models import (
    MarkEntry,
)


class MarkVerification(
    SessionBaseModel
):

    STATUS_CHOICES = [

        ("PENDING", "Pending"),

        ("VERIFIED", "Verified"),

        ("REJECTED", "Rejected"),

        ("APPROVED", "Approved"),
    ]

    mark_entry = models.OneToOneField(

        MarkEntry,

        on_delete=models.CASCADE,

        related_name="verification",
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="PENDING",
    )

    verified_by = models.ForeignKey(

        "users.User",

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="verified_marks",
    )

    verified_at = models.DateTimeField(

        null=True,

        blank=True,
    )

    rejection_reason = models.TextField(
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "mark_verifications"
        )

        ordering = [
            "-created_at",
        ]

    def __str__(self):

        return (
            f"{self.mark_entry}"
        )