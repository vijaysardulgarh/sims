from rest_framework import viewsets

from .models import (
    TimetableAuditLog,
)

from .serializers import (
    TimetableAuditLogSerializer,
)


class TimetableAuditLogViewSet(
    viewsets.ReadOnlyModelViewSet
):

    queryset = (
        TimetableAuditLog.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        TimetableAuditLogSerializer
    )

    search_fields = [
        "action",
        "field_name",
    ]

    ordering_fields = [
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]