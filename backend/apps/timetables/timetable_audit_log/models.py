from django.db import models

from apps.core.models import (
    SessionBaseModel,
)


class TimetableAuditLog(
    SessionBaseModel,
):

    ACTION_CHOICES = (
        ("CREATE", "Create"),
        ("UPDATE", "Update"),
        ("DELETE", "Delete"),
        ("APPROVE", "Approve"),
        ("PUBLISH", "Publish"),
        ("UNPUBLISH", "Unpublish"),
        ("SUBSTITUTE", "Substitute"),
    )

    timetable = models.ForeignKey(
        "timetables.Timetable",
        on_delete=models.CASCADE,
        related_name="audit_logs",
    )

    timetable_entry = models.ForeignKey(
        "timetable_entries.TimetableEntry",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs",
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES,
    )

    field_name = models.CharField(
        max_length=100,
        blank=True,
    )

    old_value = models.TextField(
        blank=True,
    )

    new_value = models.TextField(
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "tt_timetable_audit_logs"
        )

        ordering = [
            "-created_at",
        ]

    def __str__(
        self,
    ):

        return (
            f"{self.timetable} - "
            f"{self.action}"
        )