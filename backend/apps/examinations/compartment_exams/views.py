from apps.core.common.views import SchoolFilteredViewSet
from .models import (
    CompartmentExam
)

from .serializers import (
    CompartmentExamSerializer
)


class CompartmentExamViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        CompartmentExam.objects
        .select_related(
            "student",
            "subject",
            "original_exam",
        )
    )

    serializer_class = (
        CompartmentExamSerializer
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