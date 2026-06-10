from rest_framework import viewsets

from .models import (
    PeriodDefinition,
)

from .serializers import (
    PeriodDefinitionSerializer,
)


class PeriodDefinitionViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        PeriodDefinition.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        PeriodDefinitionSerializer
    )

    search_fields = [
        "name",
        "code",
    ]

    ordering_fields = [
        "display_order",
        "start_time",
        "created_at",
    ]

    ordering = [
        "display_order",
        "start_time",
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