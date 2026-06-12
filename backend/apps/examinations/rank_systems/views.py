from apps.core.common.views import SchoolFilteredViewSet

from .models import (
    RankSystem
)

from .serializers import (
    RankSystemSerializer
)


class RankSystemViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        RankSystem.objects
        .select_related(
            "exam"
        )
    )

    serializer_class = (
        RankSystemSerializer
    )

    search_fields = [

        "name",

        "exam__name",
    ]

    ordering_fields = [

        "name",

        "rank_type",

        "created_at",
    ]

    ordering = [
        "name",
    ]