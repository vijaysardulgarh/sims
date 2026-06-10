from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    MarkEntry
)

from .serializers import (
    MarkEntrySerializer
)


class MarkEntryViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        MarkEntry.objects
        .select_related(
            "student",
            "subject",
            "exam",
        )
    )

    serializer_class = (
        MarkEntrySerializer
    )

    search_fields = [

        "student__full_name",

        "subject__name",

        "exam__name",
    ]

    ordering_fields = [

        "student",

        "created_at",
    ]

    ordering = [
        "student",
    ]