from apps.core.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.classes.models import (
    Class
)

from apps.academics.classes.serializers import (
    ClassSerializer
)


class ClassViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        ClassSerializer
    )

    search_fields = [
        "name",
    ]

    ordering_fields = [
        "name",
        "display_order",
    ]

    filterset_fields = [
        "display_order",
        "is_active",
    ]

    def get_queryset(self):

        queryset = (
            Class.objects.select_related(
                "school"
            )
        )

        return self.filter_queryset_by_school(
            queryset
        )