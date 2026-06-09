from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class CommunicationCategory(
    SchoolBaseModel
):

    name = models.CharField(
        max_length=100
    )

    code = models.CharField(
        max_length=50
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    class Meta:

        db_table = "communication_categories"

        ordering = ["name"]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "name"
                ],
                name="unique_communication_category_name_per_school"
            ),

            models.UniqueConstraint(
                fields=[
                    "school",
                    "code"
                ],
                name="unique_communication_category_code_per_school"
            ),

        ]

        indexes = [

            models.Index(
                fields=[
                    "school",
                    "name"
                ]
            ),

            models.Index(
                fields=[
                    "school",
                    "code"
                ]
            ),

        ]

    def __str__(self):

        return self.name