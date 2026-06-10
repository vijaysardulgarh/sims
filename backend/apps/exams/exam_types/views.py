from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    ExamType
)

from .serializers import (
    ExamTypeSerializer
)


class ExamTypeViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        ExamType.objects.all()
    )

    serializer_class = (
        ExamTypeSerializer
    )

    search_fields = [

        "name",

        "code",
    ]

    ordering_fields = [

        "name",

        "code",

        "display_order",

        "created_at",
    ]

    ordering = [
        "display_order",
        "name",
    ]