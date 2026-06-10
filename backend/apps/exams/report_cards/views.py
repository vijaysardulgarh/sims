from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    ReportCard
)

from .serializers import (
    ReportCardSerializer
)


class ReportCardViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        ReportCard.objects
        .select_related(
            "student",
            "exam",
            "result",
        )
    )

    serializer_class = (
        ReportCardSerializer
    )

    search_fields = [

        "report_card_number",

        "student__full_name",

        "exam__name",
    ]

    ordering_fields = [

        "issue_date",

        "report_card_number",

        "created_at",
    ]

    ordering = [
        "-issue_date",
    ]