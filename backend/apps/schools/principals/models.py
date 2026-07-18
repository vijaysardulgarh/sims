from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel,
)


class Principal(SchoolBaseModel):

    name = models.CharField(
        max_length=255,
    )

    photo = models.ImageField(
        upload_to="principals/",
        blank=True,
        null=True,
    )

    qualification = models.CharField(
        max_length=255,
        blank=True,
    )

    message = models.TextField(
        blank=True,
    )

    joining_date = models.DateField(
        blank=True,
        null=True,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:

        db_table = "principals"

        verbose_name = "Principal"
        verbose_name_plural = "Principals"

        ordering = [
            "display_order",
            "name",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["school"],
                name="unique_principal_per_school",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.school})"