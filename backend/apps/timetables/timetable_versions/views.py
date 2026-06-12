from rest_framework import viewsets

from .models import (
    TimetableVersion,
)

from .serializers import (
    TimetableVersionSerializer,
)


class TimetableVersionViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        TimetableVersion.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        TimetableVersionSerializer
    )

    search_fields = [
        "version_name",
    ]

    ordering_fields = [
        "version_number",
        "created_at",
    ]

    ordering = [
        "-version_number",
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