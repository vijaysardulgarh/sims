from django.db import models
from apps.core.models import SchoolBaseModel
from apps.transport.transport_routes.models import (
    TransportRoute,
    TransportStop,
)


class TransportAssignment(SchoolBaseModel):

    student_name = models.CharField(max_length=255)

    route = models.ForeignKey(
        TransportRoute,
        on_delete=models.CASCADE
    )

    stop = models.ForeignKey(
        TransportStop,
        on_delete=models.CASCADE
    )

    pickup_point = models.CharField(max_length=255)

    monthly_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    joining_date = models.DateField()

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.student_name