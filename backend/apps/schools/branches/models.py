from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Branch(
    SchoolBaseModel
):

    name = models.CharField(
        max_length=255
    )

    code = models.CharField(
        max_length=50,
        unique=True
    )

    address = models.TextField(
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    state = models.CharField(
        max_length=100,
        blank=True
    )

    pincode = models.CharField(
        max_length=20,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    principal_name = models.CharField(
        max_length=255,
        blank=True
    )

    is_head_office = models.BooleanField(
        default=False
    )

    class Meta:

        db_table = "branches"

        verbose_name = "Branch"

        verbose_name_plural = "Branches"

        ordering = ["name"]

    def __str__(self):

        return self.name