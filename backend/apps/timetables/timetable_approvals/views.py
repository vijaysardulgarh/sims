from rest_framework import viewsets

from .models import (
    TimetableApproval,
)

from .serializers import (
    TimetableApprovalSerializer,
)


class TimetableApprovalViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        TimetableApproval.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        TimetableApprovalSerializer
    )

    search_fields = [
        "status",
    ]

    ordering_fields = [
        "created_at",
        "approved_at",
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