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
        max_length=50
    )

    description = models.TextField(
        blank=True
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

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "code"
                ],

                name=(
                    "unique_school_asset_category_code"
                )
            )
        ]

    def __str__(self):

        return (
            f"{self.code} - {self.name}"
        )