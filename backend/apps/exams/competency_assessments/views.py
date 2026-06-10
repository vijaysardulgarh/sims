from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    CompetencyAssessment
)

from .serializers import (
    CompetencyAssessmentSerializer
)


class CompetencyAssessmentViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        CompetencyAssessment.objects
        .select_related(
            "student",
            "exam",
            "subject",
        )
    )

    serializer_class = (
        CompetencyAssessmentSerializer
    )

    search_fields = [

        "student__full_name",

        "subject__name",

        "exam__name",
    ]

    ordering_fields = [

        "created_at",
    ]

    ordering = [
        "-created_at",
    ]