from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.infrastructure.buildings.models import (
    Building
)


class Floor(
    SchoolBaseModel
):

    building = models.ForeignKey(

        Building,

        on_delete=models.CASCADE,

        related_name="floors"
    )

    name = models.CharField(
        max_length=100
    )

    floor_number = models.IntegerField()

    description = models.TextField(
        blank=True
    )

    class Meta:

        db_table = "floors"

        verbose_name = "Floor"

        verbose_name_plural = "Floors"

        ordering = [
            "building",
            "floor_number"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "building",
                    "floor_number"
                ],

                name=(
                    "unique_floor_per_building"
                )
            ),

            models.UniqueConstraint(

                fields=[
                    "building",
                    "name"
                ],

                name=(
                    "unique_floor_name_per_building"
                )
            ),
        ]

        indexes = [

            models.Index(
                fields=[
                    "building"
                ]
            ),

            models.Index(
                fields=[
                    "floor_number"
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

            f"{self.building.code}"

            f" - Floor "

            f"{self.floor_number}"
        )