from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.infrastructure.asset_categories.models import (
    AssetCategory
)


class Asset(
    SchoolBaseModel
):

    STATUS_CHOICES = [

        ("AVAILABLE", "Available"),

        ("IN_USE", "In Use"),

        ("UNDER_MAINTENANCE", "Under Maintenance"),

        ("DAMAGED", "Damaged"),

        ("DISPOSED", "Disposed"),
    ]

    CONDITION_CHOICES = [

        ("NEW", "New"),

        ("GOOD", "Good"),

        ("FAIR", "Fair"),

        ("POOR", "Poor"),
    ]

    category = models.ForeignKey(

        AssetCategory,

        on_delete=models.PROTECT,

        related_name="assets"
    )

    asset_code = models.CharField(
        max_length=100
    )

    name = models.CharField(
        max_length=255
    )

    brand = models.CharField(

        max_length=255,

        blank=True
    )

    model_number = models.CharField(

        max_length=255,

        blank=True
    )

    serial_number = models.CharField(

        max_length=255,

        blank=True
    )

    purchase_date = models.DateField(

        blank=True,

        null=True
    )

    purchase_cost = models.DecimalField(

        max_digits=12,

        decimal_places=2,

        blank=True,

        null=True
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    location = models.CharField(

        max_length=255,

        blank=True
    )

    status = models.CharField(

        max_length=30,

        choices=STATUS_CHOICES,

        default="AVAILABLE"
    )

    condition = models.CharField(

        max_length=20,

        choices=CONDITION_CHOICES,

        default="GOOD"
    )

    warranty_expiry = models.DateField(

        blank=True,

        null=True
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:

        db_table = "assets"

        verbose_name = "Asset"

        verbose_name_plural = "Assets"

        ordering = [
            "asset_code"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "asset_code"
                ],

                name=(
                    "unique_school_asset_code"
                )
            ),

            models.UniqueConstraint(

                fields=[
                    "school",
                    "serial_number"
                ],

                condition=~models.Q(
                    serial_number=""
                ),

                name=(
                    "unique_school_asset_serial_number"
                )
            ),
        ]

        indexes = [

            models.Index(
                fields=[
                    "asset_code"
                ]
            ),

            models.Index(
                fields=[
                    "status"
                ]
            ),

            models.Index(
                fields=[
                    "category"
                ]
            ),
        ]

    def __str__(self):

        return (
            f"{self.asset_code} - "
            f"{self.name}"
        )