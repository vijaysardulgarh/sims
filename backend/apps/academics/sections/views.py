from apps.academics.common.base_api import (
    SchoolFilteredViewSet
)

from apps.academics.sections.models import (
    Section
)

from apps.academics.sections.serializers import (
    SectionSerializer
)


class SectionViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        SectionSerializer
    )

    search_fields = [

        "name",

        "class_obj__name",

        "stream__name",

        "medium__name",
    ]

    ordering_fields = [

        "name",

        "class_obj__class_order"
    ]

    filterset_fields = [

        "class_obj",

        "stream",

        "medium",

        "sub_stream"
    ]

    def get_queryset(self):

        queryset = (

            Section.objects

            .select_related(
                "class_obj",
                "stream",
                "medium",
                "classroom"
            )
        )

        return self.filter_queryset_by_school(
            queryset
        )