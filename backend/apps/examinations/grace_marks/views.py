from apps.core.common.views import SchoolFilteredViewSet

from .models import (
    GraceMark
)

from .serializers import (
    GraceMarkSerializer
)


class GraceMarkViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        GraceMark.objects
        .select_related(
            "exam",
            "student",
            "subject",
        )
    )

    serializer_class = (
        GraceMarkSerializer
    )

    search_fields = [

        "student__full_name",

        "subject__name",

        "exam__name",
    ]

    ordering_fields = [

        "created_at",

        "final_marks",

        "grace_marks",
    ]

    ordering = [
        "-created_at",
    ]