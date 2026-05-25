from rest_framework import generics

from .models import Module

from .serializers import (
    ModuleSerializer
)


class ModuleListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = Module.objects.all()

    serializer_class = (
        ModuleSerializer
    )


class ModuleRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Module.objects.all()

    serializer_class = (
        ModuleSerializer
    )