from rest_framework import viewsets

from .models import (
    SubstituteAssignment,
)

from .serializers import (
    SubstituteAssignmentSerializer,
)


class SubstituteAssignmentViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        SubstituteAssignment.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        SubstituteAssignmentSerializer
    )

    search_fields = [
        "original_teacher__first_name",
        "substitute_teacher__first_name",
    ]

    ordering_fields = [
        "substitution_date",
        "created_at",
    ]

    ordering = [
        "-substitution_date",
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