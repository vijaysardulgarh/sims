from django.db import models


class Vehicle(models.Model):

    VEHICLE_TYPES = (
        ("bus", "Bus"),
        ("van", "Van"),
        ("mini_bus", "Mini Bus"),
    )

    vehicle_number = models.CharField(
        max_length=50,
        unique=True
    )

    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLE_TYPES
    )

    registration_number = models.CharField(
        max_length=100,
        unique=True
    )

    capacity = models.PositiveIntegerField()

    model = models.CharField(
        max_length=100,
        blank=True
    )

    manufacturer = models.CharField(
        max_length=100,
        blank=True
    )

    insurance_expiry = models.DateField(
        null=True,
        blank=True
    )

    pollution_expiry = models.DateField(
        null=True,
        blank=True
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["vehicle_number"]

    def __str__(self):
        return self.vehicle_number