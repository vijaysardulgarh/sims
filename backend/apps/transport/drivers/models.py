from django.db import models
from apps.core.common.base.models import SchoolBaseModel

class Driver(SchoolBaseModel):

    full_name = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    license_number = models.CharField(
        max_length=100,
        unique=True
    )

    license_expiry = models.DateField()

    address = models.TextField(blank=True)

    joining_date = models.DateField(
        null=True,
        blank=True
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name