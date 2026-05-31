from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class ComplianceDocument(
    SchoolBaseModel
):

    DOCUMENT_TYPE_CHOICES = [

        (
            "AFFILIATION_LETTER",
            "Affiliation Letter"
        ),

        (
            "NOC",
            "No Objection Certificate"
        ),

        (
            "RECOGNITION_CERTIFICATE",
            "Recognition Certificate"
        ),

        (
            "BUILDING_SAFETY",
            "Building Safety Certificate"
        ),

        (
            "FIRE_SAFETY",
            "Fire Safety Certificate"
        ),

        (
            "WATER_SANITATION",
            "Water & Sanitation Certificate"
        ),

        (
            "DEO_CERTIFICATE",
            "DEO Certificate"
        ),

        (
            "FEE_STRUCTURE",
            "Fee Structure"
        ),

        (
            "ACADEMIC_CALENDAR",
            "Academic Calendar"
        ),

        (
            "SMC_LIST",
            "School Management Committee"
        ),

        (
            "PTA_LIST",
            "Parent Teacher Association"
        ),

        (
            "BOARD_RESULTS",
            "Board Results"
        ),
    ]

    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPE_CHOICES
    )

    title = models.CharField(
        max_length=255
    )

    document = models.FileField(
        upload_to="compliance/"
    )

    issue_date = models.DateField(
        blank=True,
        null=True
    )

    expiry_date = models.DateField(
        blank=True,
        null=True
    )

    issuing_authority = (
        models.CharField(
            max_length=255,
            blank=True
        )
    )

    remarks = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = (
            "compliance_documents"
        )

        verbose_name = (
            "Compliance Document"
        )

        verbose_name_plural = (
            "Compliance Documents"
        )

        ordering = [
            "document_type",
            "title"
        ]

    def __str__(self):

        return self.title