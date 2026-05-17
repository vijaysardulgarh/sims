from rest_framework import generics

from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = Vehicle.objects.all()

    serializer_class = VehicleSerializer


class VehicleRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Vehicle.objects.all()

    serializer_class = VehicleSerializer