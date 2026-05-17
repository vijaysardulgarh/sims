from rest_framework import generics

from .models import TransportAssignment

from .serializers import (
    TransportAssignmentSerializer,
)


class TransportAssignmentListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = TransportAssignment.objects.all()

    serializer_class = TransportAssignmentSerializer


class TransportAssignmentRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = TransportAssignment.objects.all()

    serializer_class = TransportAssignmentSerializer