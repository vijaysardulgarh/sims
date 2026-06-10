from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    DateSheet
)

from .serializers import (
    DateSheetSerializer
)


class DateSheetViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        DateSheet.objects
        .select_related(
            "exam",
            "class_obj",
            "section",
            "subject",
            "invigilator",
        )
    )

    serializer_class = (
        DateSheetSerializer
    )

    search_fields = [

        "exam__name",

        "subject__name",

        "class_obj__name",

        "section__name",
    ]

    ordering_fields = [

        "exam_date",

        "start_time",

        "end_time",

        "created_at",
    ]

    ordering = [
        "exam_date",
        "start_time",
    ]