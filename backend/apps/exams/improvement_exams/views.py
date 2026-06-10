from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    ImprovementExam
)

from .serializers import (
    ImprovementExamSerializer
)


class ImprovementExamViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        ImprovementExam.objects
        .select_related(
            "student",
            "subject",
            "original_exam",
        )
    )

    serializer_class = (
        ImprovementExamSerializer
    )

    search_fields = [

        "student__full_name",

        "subject__name",

        "original_exam__name",
    ]

    ordering_fields = [

        "exam_date",

        "registration_date",

        "created_at",
    ]

    ordering = [
        "-exam_date",
    ]