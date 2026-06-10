from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    InternalAssessment
)

from .serializers import (
    InternalAssessmentSerializer
)


class InternalAssessmentViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        InternalAssessment.objects
        .select_related(
            "student",
            "subject",
            "exam",
        )
    )

    serializer_class = (
        InternalAssessmentSerializer
    )

    search_fields = [

        "student__full_name",

        "subject__name",

        "exam__name",
    ]

    ordering_fields = [

        "total_marks",

        "created_at",
    ]

    ordering = [
        "-created_at",
    ]