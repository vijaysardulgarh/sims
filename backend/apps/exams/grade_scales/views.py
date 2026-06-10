from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    GradeScale
)

from .serializers import (
    GradeScaleSerializer
)


class GradeScaleViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        GradeScale.objects.all()
    )

    serializer_class = (
        GradeScaleSerializer
    )

    search_fields = [

        "name",

        "code",
    ]

    ordering_fields = [

        "name",

        "code",

        "created_at",
    ]

    ordering = [
        "name",
    ]