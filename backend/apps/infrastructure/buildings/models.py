from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Building(
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

    number_of_floors = (
        models.PositiveIntegerField(
            default=1
        )
    )

    class Meta:

        db_table = "buildings"

        verbose_name = "Building"

        verbose_name_plural = (
            "Buildings"
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
                    "unique_school_building_code"
                )
            )
        ]

        indexes = [

            models.Index(
                fields=[
                    "code"
                ]
            ),

            models.Index(
                fields=[
                    "name"
                ]
            ),
        ]

    def __str__(self):

        return (
            f"{self.code} - "
            f"{self.name}"
        )