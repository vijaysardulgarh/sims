from rest_framework import viewsets

from .models import (
    Timetable,
)

from .serializers import (
    TimetableSerializer,
)


class TimetableViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Timetable.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        TimetableSerializer
    )

    search_fields = [
        "name",
        "code",
    ]

    ordering_fields = [
        "created_at",
        "effective_from",
    ]

    ordering = [
        "school_class",
        "section",
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