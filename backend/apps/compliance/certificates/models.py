from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Certificate(
    SchoolBaseModel
):

    CERTIFICATE_TYPE_CHOICES = [

        (
            "FIRE_SAFETY",
            "Fire Safety Certificate"
        ),

        (
            "BUILDING_SAFETY",
            "Building Safety Certificate"
        ),

        (
            "WATER_SANITATION",
            "Water & Sanitation Certificate"
        ),

        (
            "HEALTH",
            "Health Certificate"
        ),

        (
            "ELECTRICAL",
            "Electrical Safety Certificate"
        ),

        (
            "STRUCTURAL",
            "Structural Stability Certificate"
        ),

        (
            "LIFT_SAFETY",
            "Lift Safety Certificate"
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

    certificate_type = models.CharField(
        max_length=50,
        choices=CERTIFICATE_TYPE_CHOICES
    )

    certificate_number = models.CharField(
        max_length=100
    )

    issuing_authority = models.CharField(
        max_length=255
    )

    document = models.FileField(
        upload_to="certificates/",
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

        db_table = "certificates"

        verbose_name = "Certificate"

        verbose_name_plural = (
            "Certificates"
        )

        ordering = [
            "certificate_type"
        ]

    def __str__(self):

        return (
            f"{self.school.name} - "
            f"{self.certificate_type}"
        )