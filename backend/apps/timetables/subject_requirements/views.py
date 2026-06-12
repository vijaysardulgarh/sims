from rest_framework import viewsets

from .models import (
    SubjectRequirement,
)

from .serializers import (
    SubjectRequirementSerializer,
)


class SubjectRequirementViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        SubjectRequirement.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        SubjectRequirementSerializer
    )

    search_fields = [
        "subject__name",
    ]

    ordering_fields = [
        "created_at",
        "periods_per_week",
    ]

    ordering = [
        "school_class",
        "subject",
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