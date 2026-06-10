from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    ResultApproval
)

from .serializers import (
    ResultApprovalSerializer
)


class ResultApprovalViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        ResultApproval.objects
        .select_related(
            "result",
            "result__student",
            "result__exam",
            "approved_by",
        )
    )

    serializer_class = (
        ResultApprovalSerializer
    )

    search_fields = [

        "result__student__full_name",

        "result__exam__name",
    ]

    ordering_fields = [

        "status",

        "approved_at",

        "created_at",
    ]

    ordering = [
        "-created_at",
    ]