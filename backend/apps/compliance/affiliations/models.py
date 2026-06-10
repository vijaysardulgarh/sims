from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Affiliation(
    SchoolBaseModel
):

    BOARD_CHOICES = [

        ("CBSE", "CBSE"),

        ("STATE", "State Board"),

        ("ICSE", "ICSE"),

        ("IB", "IB"),

        ("CAMBRIDGE", "Cambridge"),
    ]

    STATUS_CHOICES = [

        ("ACTIVE", "Active"),

        ("EXPIRED", "Expired"),

        ("PENDING", "Pending"),

        ("SUSPENDED", "Suspended"),
    ]

    board = models.CharField(

        max_length=50,

        choices=BOARD_CHOICES
    )

    affiliation_number = models.CharField(

        max_length=100
    )

    affiliation_letter = models.FileField(

        upload_to="affiliations/",

        blank=True,

        null=True
    )

    issue_date = models.DateField(

        blank=True,

        null=True
    )

    valid_upto = models.DateField(

        blank=True,

        null=True
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="ACTIVE"
    )

    remarks = models.TextField(

        blank=True
    )

    class Meta:

        db_table = "affiliations"

        verbose_name = "Affiliation"

        verbose_name_plural = "Affiliations"

        ordering = [
            "board"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "board",
                    "affiliation_number"
                ],
                name="unique_affiliation_per_school"
            )

        ]