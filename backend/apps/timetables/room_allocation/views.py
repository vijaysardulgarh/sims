from rest_framework import viewsets

from .models import (
    RoomAllocation,
)

from .serializers import (
    RoomAllocationSerializer,
)


class RoomAllocationViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        RoomAllocation.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        RoomAllocationSerializer
    )

    search_fields = [
        "room__name",
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