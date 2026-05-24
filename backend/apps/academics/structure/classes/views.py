from apps.core.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.structure.classes.models import (
    Class
)

from apps.academics.structure.classes.serializers import (
    ClassSerializer
)


class ClassViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        ClassSerializer
    )

    search_fields = [
        "name"
    ]

    ordering_fields = [
        "name",
        "class_order"
    ]

    filterset_fields = [
        "class_order"
    ]

    def get_queryset(self):

        queryset = (
            Class.objects.all()
        )

        return self.filter_queryset_by_school(
            queryset
        )