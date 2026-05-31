from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Facility(
    SchoolBaseModel
):

    FACILITY_TYPE_CHOICES = [

        ("CCTV", "CCTV"),

        ("WIFI", "WiFi"),

        ("RO_WATER", "RO Water"),

        ("MEDICAL_ROOM", "Medical Room"),

        ("TRANSPORT", "Transport"),

        ("HOSTEL", "Hostel"),

        ("POWER_BACKUP", "Power Backup"),

        ("BIOMETRIC", "Biometric System"),

        ("PA_SYSTEM", "Public Address System"),

        ("OTHER", "Other"),
    ]

    name = models.CharField(
        max_length=255
    )

    facility_type = models.CharField(
        max_length=30,
        choices=FACILITY_TYPE_CHOICES
    )

    description = models.TextField(
        blank=True
    )

    available = models.BooleanField(
        default=True
    )

    installation_date = models.DateField(
        blank=True,
        null=True
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:

        db_table = "facilities"

        verbose_name = "Facility"

        verbose_name_plural = "Facilities"

        ordering = [
            "name"
        ]

    def __str__(self):

        return self.name