from rest_framework import filters
from rest_framework import viewsets

from .models import BellSchedule
from .serializers import BellScheduleSerializer


class BellScheduleViewSet(
    viewsets.ModelViewSet
):

    queryset = BellSchedule.objects.filter(
        is_deleted=False,
    )

    serializer_class = BellScheduleSerializer

    search_fields = [
        "name",
        "code",
    ]

    ordering_fields = [
        "name",
        "code",
        "created_at",
    ]

    ordering = [
        "display_order",
        "name",
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

        instance.deleted_by = self.request.user

        instance.save()