from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    SeatingPlan
)

from .serializers import (
    SeatingPlanSerializer
)


class SeatingPlanViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        SeatingPlan.objects
        .select_related(
            "student",
            "exam",
        )
    )

    serializer_class = (
        SeatingPlanSerializer
    )

    search_fields = [

        "student__full_name",

        "room_number",

        "seat_number",

        "exam__name",
    ]

    ordering_fields = [

        "room_number",

        "row_number",

        "seat_number",

        "created_at",
    ]

    ordering = [

        "room_number",

        "row_number",
    ]