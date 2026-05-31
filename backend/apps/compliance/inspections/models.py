from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Inspection(
    SchoolBaseModel
):

    INSPECTION_TYPE_CHOICES = [

        (
            "CBSE",
            "CBSE Inspection"
        ),

        (
            "EDUCATION_DEPARTMENT",
            "Education Department Inspection"
        ),

        (
            "FIRE",
            "Fire Safety Inspection"
        ),

        (
            "HEALTH",
            "Health Inspection"
        ),

        (
            "BUILDING",
            "Building Safety Inspection"
        ),

        (
            "WATER_SANITATION",
            "Water & Sanitation Inspection"
        ),

        (
            "OTHER",
            "Other"
        ),
    ]

    STATUS_CHOICES = [

        (
            "PASSED",
            "Passed"
        ),

        (
            "FAILED",
            "Failed"
        ),

        (
            "PENDING",
            "Pending"
        ),

        (
            "CONDITIONAL",
            "Conditional Approval"
        ),
    ]

    inspection_type = models.CharField(
        max_length=50,
        choices=INSPECTION_TYPE_CHOICES
    )

    inspection_date = models.DateField()

    authority = models.CharField(
        max_length=255
    )

    officer_name = models.CharField(
        max_length=255,
        blank=True
    )

    report_number = models.CharField(
        max_length=100,
        blank=True
    )

    document = models.FileField(
        upload_to="inspections/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PASSED"
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:

        db_table = "inspections"

        verbose_name = "Inspection"

        verbose_name_plural = (
            "Inspections"
        )

        ordering = [
            "-inspection_date"
        ]

    def __str__(self):

        return (
            f"{self.school.name} - "
            f"{self.inspection_type}"
        )