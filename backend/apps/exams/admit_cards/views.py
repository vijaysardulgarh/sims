from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    AdmitCard
)

from .serializers import (
    AdmitCardSerializer
)


class AdmitCardViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        AdmitCard.objects
        .select_related(
            "student",
            "exam",
        )
    )

    serializer_class = (
        AdmitCardSerializer
    )

    search_fields = [

        "roll_number",

        "student__full_name",

        "exam__name",
    ]

    ordering_fields = [

        "issue_date",

        "roll_number",

        "created_at",
    ]

    ordering = [
        "-issue_date",
    ]