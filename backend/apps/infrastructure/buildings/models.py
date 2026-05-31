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
        max_length=50,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    number_of_floors = (
        models.PositiveIntegerField(
            default=1
        )
    )

    is_active = models.BooleanField(
        default=True
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

    def __str__(self):

        return (
            f"{self.name}"
        )