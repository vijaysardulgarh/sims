from rest_framework import viewsets

from .models import (
    WorkingDay,
)

from .serializers import (
    WorkingDaySerializer,
)


class WorkingDayViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        WorkingDay.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        WorkingDaySerializer
    )

    search_fields = [
        "day_code",
    ]

    ordering_fields = [
        "display_order",
        "created_at",
    ]

    ordering = [
        "display_order",
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