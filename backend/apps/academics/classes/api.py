from apps.academics.common.base_api import (
    SchoolFilteredViewSet
)

from apps.academics.classes import (
    Class
)

from apps.academics.classes.serializer import (
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

        return (
            self.filter_queryset_by_school(
                queryset
            )
        )