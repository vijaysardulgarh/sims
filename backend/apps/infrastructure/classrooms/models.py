from django.db import models

from django.core.exceptions import ValidationError

from apps.core.common.base.models import SchoolBaseModel


class Classroom(
    SchoolBaseModel
):

    name = models.CharField(
        max_length=50,
        db_index=True
    )

    capacity = models.PositiveIntegerField(
        default=40
    )

    floor = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def clean(self):

        if self.name:

            self.name = (
                self.name.strip().upper()
            )

        if self.floor:

            self.floor = (
                self.floor.strip()
            )

        if self.capacity <= 0:

            raise ValidationError(
                {
                    "capacity":
                        "Capacity must be greater than 0."
                }
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        ordering = [
            "name"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "name"
                ],
                name="unique_classroom_per_school"
            )
        ]

    def __str__(self):

        return self.name