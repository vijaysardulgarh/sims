from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    MarkVerification
)

from .serializers import (
    MarkVerificationSerializer
)


class MarkVerificationViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        MarkVerification.objects
        .select_related(
            "mark_entry",
            "mark_entry__student",
            "mark_entry__subject",
            "mark_entry__exam",
            "verified_by",
        )
    )

    serializer_class = (
        MarkVerificationSerializer
    )

    search_fields = [

        "mark_entry__student__full_name",

        "mark_entry__subject__name",

        "mark_entry__exam__name",
    ]

    ordering_fields = [

        "status",

        "verified_at",

        "created_at",
    ]

    ordering = [
        "-created_at",
    ]