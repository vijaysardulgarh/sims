from django.db import models
from django.core.exceptions import ValidationError

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.infrastructure.assets.models import (
    Asset
)


class MaintenanceRecord(
    SchoolBaseModel
):

    SERVICE_TYPE_CHOICES = [

        (
            "PREVENTIVE",
            "Preventive Maintenance"
        ),

        (
            "CORRECTIVE",
            "Corrective Maintenance"
        ),

        (
            "REPAIR",
            "Repair"
        ),

        (
            "INSPECTION",
            "Inspection"
        ),

        (
            "OTHER",
            "Other"
        ),
    ]

    asset = models.ForeignKey(

        Asset,

        on_delete=models.CASCADE,

        related_name="maintenance_records"
    )

    maintenance_date = models.DateField()

    service_type = models.CharField(

        max_length=20,

        choices=SERVICE_TYPE_CHOICES
    )

    vendor_name = models.CharField(

        max_length=255,

        blank=True
    )

    cost = models.DecimalField(

        max_digits=12,

        decimal_places=2,

        blank=True,

        null=True
    )

    next_due_date = models.DateField(

        blank=True,

        null=True
    )

    remarks = models.TextField(
        blank=True
    )

    def clean(self):

        if (
            self.asset
            and self.school
            and self.asset.school_id
            != self.school_id
        ):

            raise ValidationError(
                "Asset must belong to the same school."
            )

        if (
            self.next_due_date
            and
            self.next_due_date
            <
            self.maintenance_date
        ):

            raise ValidationError(
                "Next due date cannot be before maintenance date."
            )

    class Meta:

        db_table = (
            "maintenance_records"
        )

        verbose_name = (
            "Maintenance Record"
        )

        verbose_name_plural = (
            "Maintenance Records"
        )

        ordering = [
            "-maintenance_date"
        ]

        indexes = [

            models.Index(
                fields=[
                    "asset"
                ]
            ),

            models.Index(
                fields=[
                    "maintenance_date"
                ]
            ),

            models.Index(
                fields=[
                    "next_due_date"
                ]
            ),

            models.Index(
                fields=[
                    "service_type"
                ]
            ),

            models.Index(
                fields=[
                    "school"
                ]
            ),
        ]

    def __str__(self):

        return (

            f"{self.asset.asset_code}"

            f" - "

            f"{self.maintenance_date}"
        )