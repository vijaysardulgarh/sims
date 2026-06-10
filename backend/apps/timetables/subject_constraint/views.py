from rest_framework import viewsets

from .models import (
    SubjectConstraint,
)

from .serializers import (
    SubjectConstraintSerializer,
)


class SubjectConstraintViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        SubjectConstraint.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        SubjectConstraintSerializer
    )

    search_fields = [
        "subject__name",
    ]

    ordering_fields = [
        "created_at",
    ]

    ordering = [
        "subject__name",
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