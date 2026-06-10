from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    Revaluation
)

from .serializers import (
    RevaluationSerializer
)


class RevaluationViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        Revaluation.objects
        .select_related(
            "student",
            "subject",
            "exam",
            "reviewed_by",
        )
    )

    serializer_class = (
        RevaluationSerializer
    )

    search_fields = [

        "student__full_name",

        "subject__name",

        "exam__name",
    ]

    ordering_fields = [

        "request_date",

        "status",

        "created_at",
    ]

    ordering = [
        "-request_date",
    ]