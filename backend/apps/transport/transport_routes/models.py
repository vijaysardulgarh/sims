from django.db import models

from apps.transport.vehicles.models import Vehicle
from apps.transport.drivers.models import Driver


class TransportRoute(models.Model):

    route_name = models.CharField(max_length=255)

    start_location = models.CharField(max_length=255)

    end_location = models.CharField(max_length=255)

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.route_name


class TransportStop(models.Model):

    route = models.ForeignKey(
        TransportRoute,
        on_delete=models.CASCADE,
        related_name="stops"
    )

    stop_name = models.CharField(max_length=255)

    pickup_time = models.TimeField()

    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.stop_name