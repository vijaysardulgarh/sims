from apps.core.common.views import SchoolFilteredViewSet

from .models import (
    ResultPublication
)

from .serializers import (
    ResultPublicationSerializer
)


class ResultPublicationViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        ResultPublication.objects
        .select_related(
            "exam",
            "published_by",
        )
    )

    serializer_class = (
        ResultPublicationSerializer
    )

    search_fields = [

        "exam__name",
    ]

    ordering_fields = [

        "publication_date",

        "published_at",

        "created_at",
    ]

    ordering = [
        "-publication_date",
    ]