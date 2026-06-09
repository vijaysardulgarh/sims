from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Circular(
    SchoolBaseModel
):

    CIRCULAR_TYPE_CHOICES = [

        (
            "GOVERNMENT",
            "Government Circular"
        ),

        (
            "CBSE",
            "CBSE Circular"
        ),

        (
            "ADMINISTRATIVE",
            "Administrative Circular"
        ),

        (
            "POLICY",
            "Policy Circular"
        ),

        (
            "DEPARTMENT",
            "Department Circular"
        ),

        (
            "OTHER",
            "Other"
        ),
    ]

    title = models.CharField(
        max_length=255
    )

    circular_type = models.CharField(
        max_length=30,
        choices=CIRCULAR_TYPE_CHOICES,
        default="OTHER"
    )

    reference_number = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField()

    attachment = models.FileField(
        upload_to="circulars/",
        blank=True,
        null=True
    )

    issue_date = models.DateField()

    effective_date = models.DateField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "circulars"

        verbose_name = "Circular"

        verbose_name_plural = "Circulars"

        ordering = [
            "-issue_date"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "title"
                ],
                name="unique_circular_title_per_school"
            ),

        ]

        indexes = [

            models.Index(
                fields=[
                    "school",
                    "issue_date"
                ]
            ),

            models.Index(
                fields=[
                    "school",
                    "circular_type"
                ]
            ),

            models.Index(
                fields=[
                    "school",
                    "is_active"
                ]
            ),

        ]

    def __str__(self):

        return self.title