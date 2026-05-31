from django.db import models

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

    def __str__(self):

        return (

            f"{self.asset.name} - "

            f"{self.maintenance_date}"
        )