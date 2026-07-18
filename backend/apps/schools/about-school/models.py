from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class AboutSchool(
    SchoolBaseModel
):

    history = models.TextField(
        blank=True
    )

    vision = models.TextField(
        blank=True
    )

    mission = models.TextField(
        blank=True
    )

    def __str__(self):

        return (
            f"About {self.school.name}"
        )

    class Meta:

        db_table = "about_schools"

        verbose_name = "About School"

        verbose_name_plural = (
            "About Schools"
        )

        constraints = [

            models.UniqueConstraint(
                fields=["school"],
                name="unique_about_school_per_school"
            )

        ]