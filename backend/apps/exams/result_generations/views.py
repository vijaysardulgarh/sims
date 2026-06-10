from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    ResultGeneration
)

from .serializers import (
    ResultGenerationSerializer
)


class ResultGenerationViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        ResultGeneration.objects
        .select_related(
            "student",
            "exam",
        )
    )

    serializer_class = (
        ResultGenerationSerializer
    )

    search_fields = [

        "student__full_name",

        "exam__name",

        "overall_grade",
    ]

    ordering_fields = [

        "percentage",

        "class_rank",

        "section_rank",

        "school_rank",

        "created_at",
    ]

    ordering = [
        "-percentage",
    ]