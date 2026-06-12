from rest_framework import viewsets

from .models import (
    TimetablePublication,
)

from .serializers import (
    TimetablePublicationSerializer,
)


class TimetablePublicationViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        TimetablePublication.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        TimetablePublicationSerializer
    )

    search_fields = [
        "status",
    ]

    ordering_fields = [
        "created_at",
        "published_at",
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