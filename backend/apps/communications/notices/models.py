from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Notice(
    SchoolBaseModel
):

    NOTICE_TYPE_CHOICES = [

        ("GENERAL", "General"),

        ("HOLIDAY", "Holiday"),

        ("EXAM", "Exam"),

        ("FEE", "Fee"),

        ("ADMISSION", "Admission"),

        ("STAFF", "Staff"),

        ("TRANSPORT", "Transport"),

        ("URGENT", "Urgent"),
    ]

    title = models.CharField(
        max_length=255
    )

    notice_type = models.CharField(
        max_length=20,
        choices=NOTICE_TYPE_CHOICES,
        default="GENERAL"
    )

    description = models.TextField()

    attachment = models.FileField(
        upload_to="notices/",
        blank=True,
        null=True
    )

    publish_date = models.DateField()

    expiry_date = models.DateField(
        blank=True,
        null=True
    )

    is_published = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "notices"

        verbose_name = "Notice"

        verbose_name_plural = "Notices"

        ordering = [
            "-publish_date"
        ]

    def __str__(self):

        return self.title