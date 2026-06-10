from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    Exam
)

from .serializers import (
    ExamSerializer
)


class ExamViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        Exam.objects.select_related(
            "exam_type"
        )
    )

    serializer_class = (
        ExamSerializer
    )

    search_fields = [

        "name",

        "exam_type__name",
    ]

    ordering_fields = [

        "name",

        "start_date",

        "end_date",

        "created_at",
    ]

    ordering = [
        "-start_date",
    ]