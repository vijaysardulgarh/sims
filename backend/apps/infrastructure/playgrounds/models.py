from django.db import models
from django.core.exceptions import ValidationError

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Playground(
    SchoolBaseModel
):

    PLAYGROUND_TYPE_CHOICES = [

        ("CRICKET", "Cricket Ground"),

        ("FOOTBALL", "Football Ground"),

        ("BASKETBALL", "Basketball Court"),

        ("VOLLEYBALL", "Volleyball Court"),

        ("BADMINTON", "Badminton Court"),

        ("ATHLETICS", "Athletics Track"),

        ("MULTIPURPOSE", "Multi Purpose Ground"),

        ("OTHER", "Other"),
    ]

    name = models.CharField(
        max_length=255
    )

    playground_type = models.CharField(
        max_length=30,
        choices=PLAYGROUND_TYPE_CHOICES
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    capacity = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    covered = models.BooleanField(
        default=False
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    def clean(self):

        if (
            self.area is not None
            and self.area <= 0
        ):

            raise ValidationError(
                "Area must be greater than zero."
            )

        if (
            self.capacity is not None
            and self.capacity <= 0
        ):

            raise ValidationError(
                "Capacity must be greater than zero."
            )

    class Meta:

        db_table = "playgrounds"

        verbose_name = "Playground"

        verbose_name_plural = "Playgrounds"

        ordering = [
            "name"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "name"
                ],

                name=(
                    "unique_school_playground_name"
                )
            )
        ]

        indexes = [

            models.Index(
                fields=[
                    "school"
                ]
            ),

            models.Index(
                fields=[
                    "playground_type"
                ]
            ),
        ]

    def __str__(self):

        return (
            f"{self.name}"
        )