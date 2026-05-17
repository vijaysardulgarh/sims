from rest_framework import serializers

from .models import (
    TransportRoute,
    TransportStop,
)


class TransportStopSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = TransportStop
        fields = "__all__"


class TransportRouteSerializer(
    serializers.ModelSerializer
):

    stops = TransportStopSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = TransportRoute
        fields = "__all__"