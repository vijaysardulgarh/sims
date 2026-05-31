from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class AssetCategory(
    SchoolBaseModel
):

    name = models.CharField(
        max_length=255
    )

    code = models.CharField(
        max_length=50,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "asset_categories"

        verbose_name = "Asset Category"

        verbose_name_plural = (
            "Asset Categories"
        )

        ordering = [
            "name"
        ]

    def __str__(self):

        return self.name