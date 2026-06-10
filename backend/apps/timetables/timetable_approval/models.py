from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class TimetableApproval(
    SessionBaseModel,
):

    STATUS_CHOICES = (
        ("DRAFT", "Draft"),
        ("SUBMITTED", "Submitted"),
        ("UNDER_REVIEW", "Under Review"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    )

    timetable = models.ForeignKey(
        "timetables.Timetable",
        on_delete=models.CASCADE,
        related_name="approvals",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DRAFT",
    )

    approved_by = models.ForeignKey(
        "employees.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_timetables",
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_timetable_approvals"
        )

        ordering = [
            "-created_at",
        ]

    def __str__(
        self,
    ):

        return (
            f"{self.timetable} - "
            f"{self.status}"
        )