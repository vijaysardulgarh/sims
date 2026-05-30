from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Module

from .serializers import (
    ModuleSerializer
)


# =========================================
# MODULE LIST + CREATE
# =========================================

class ModuleListCreateAPIView(
    generics.ListCreateAPIView
):

    serializer_class = (
        ModuleSerializer
    )

    def get_queryset(self):

        return Module.objects.filter(

            is_deleted=False,
            parent__isnull=True,

        ).select_related(

            "parent"

        ).prefetch_related(

            "children"

        ).order_by(

            "order",
            "name",
        )

    # =====================================
    # DEBUG CREATE
    # =====================================

    def create(self, request, *args, **kwargs):

        print("REQUEST DATA:")
        print(request.data)

        serializer = self.get_serializer(
            data=request.data
        )

        if not serializer.is_valid():

            print("SERIALIZER ERRORS:")
            print(serializer.errors)

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


# =========================================
# MODULE DETAIL
# =========================================

class ModuleRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = (
        ModuleSerializer
    )

    def get_queryset(self):

        return Module.objects.filter(

            is_deleted=False

        ).select_related(

            "parent"

        ).prefetch_related(

            "children"

        )