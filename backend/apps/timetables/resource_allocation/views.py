from rest_framework import viewsets

from .models import (
    ResourceAllocation,
)

from .serializers import (
    ResourceAllocationSerializer,
)


class ResourceAllocationViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        ResourceAllocation.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        ResourceAllocationSerializer
    )

    search_fields = [
        "resource__name",
    ]

    ordering_fields = [
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]

    def perform_create(
        self,
        serializer,
    ):

        serializer.save(
            created_by=self.request.user,
        )

    def perform_update(
        self,
        serializer,
    ):

        serializer.save(
            updated_by=self.request.user,
        )

    def perform_destroy(
        self,
        instance,
    ):

        instance.is_deleted = True

        instance.deleted_by = (
            self.request.user
        )

        instance.save()