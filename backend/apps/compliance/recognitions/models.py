from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Recognition(SchoolBaseModel):

    RECOGNITION_TYPE_CHOICES = [

        (
            "SCHOOL_RECOGNITION",
            "School Recognition"
        ),

        (
            "RTE_RECOGNITION",
            "RTE Recognition"
        ),

        (
            "GOVERNMENT_APPROVAL",
            "Government Approval"
        ),

        (
            "MINORITY_STATUS",
            "Minority Status"
        ),

        (
            "OTHER",
            "Other"
        ),
    ]

    STATUS_CHOICES = [

        ("ACTIVE", "Active"),

        ("EXPIRED", "Expired"),

        ("PENDING", "Pending"),
    ]

    recognition_type = models.CharField(
        max_length=50,
        choices=RECOGNITION_TYPE_CHOICES
    )

    recognition_number = models.CharField(
        max_length=100
    )

    issuing_authority = models.CharField(
        max_length=255
    )

    recognition_document = models.FileField(
        upload_to="recognitions/",
        blank=True,
        null=True
    )

    issue_date = models.DateField(
        blank=True,
        null=True
    )

    valid_upto = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:

        db_table = "recognitions"

        verbose_name = "Recognition"

        verbose_name_plural = "Recognitions"

        ordering = [
            "recognition_type"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "recognition_number"
                ],
                name="unique_recognition_per_school"
            )

        ]