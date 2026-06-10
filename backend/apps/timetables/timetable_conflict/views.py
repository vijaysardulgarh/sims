from rest_framework import viewsets

from .models import (
    TimetableConflict,
)

from .serializers import (
    TimetableConflictSerializer,
)


class TimetableConflictViewSet(
    viewsets.ReadOnlyModelViewSet
):

    queryset = (
        TimetableConflict.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        TimetableConflictSerializer
    )

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "is_resolved",
    ]

    ordering = [
        "-created_at",
    ]