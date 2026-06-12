from apps.core.common.views import SchoolFilteredViewSet

from .models import (
    GradeCalculation
)

from .serializers import (
    GradeCalculationSerializer
)


class GradeCalculationViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        GradeCalculation.objects.all()
    )

    serializer_class = (
        GradeCalculationSerializer
    )

    search_fields = [

        "grade",
    ]

    ordering_fields = [

        "minimum_percentage",

        "maximum_percentage",

        "grade_point",

        "created_at",
    ]

    ordering = [
        "-minimum_percentage",
    ]