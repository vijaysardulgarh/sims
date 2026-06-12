from apps.core.common.views import SchoolFilteredViewSet

from .models import (
    PracticalExam
)

from .serializers import (
    PracticalExamSerializer
)


class PracticalExamViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        PracticalExam.objects
        .select_related(
            "student",
            "subject",
            "exam",
            "examiner",
        )
    )

    serializer_class = (
        PracticalExamSerializer
    )

    search_fields = [

        "student__full_name",

        "subject__name",

        "exam__name",
    ]

    ordering_fields = [

        "practical_date",

        "total_marks",

        "created_at",
    ]

    ordering = [
        "-practical_date",
    ]