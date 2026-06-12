from apps.core.common.views import SchoolFilteredViewSet

from .models import (
    BestOfSubject
)

from .serializers import (
    BestOfSubjectSerializer
)


class BestOfSubjectViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        BestOfSubject.objects
        .select_related(
            "exam"
        )
    )

    serializer_class = (
        BestOfSubjectSerializer
    )

    search_fields = [

        "name",

        "exam__name",
    ]

    ordering_fields = [

        "name",

        "subject_count",

        "created_at",
    ]

    ordering = [
        "name",
    ]