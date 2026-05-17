from rest_framework import generics

from .models import (
    TransportRoute,
    TransportStop,
)

from .serializers import (
    TransportRouteSerializer,
    TransportStopSerializer,
)


class TransportRouteListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = TransportRoute.objects.all()

    serializer_class = TransportRouteSerializer


class TransportRouteRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = TransportRoute.objects.all()

    serializer_class = TransportRouteSerializer


class TransportStopListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = TransportStop.objects.all()

    serializer_class = TransportStopSerializer