from apps.core.common.views import (
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

        "class_obj__display_order",
    ]

    filterset_fields = [

        "class_obj",

        "stream",

        "medium",

        "sub_stream",

        "is_active",
    ]

    def get_queryset(self):

        queryset = (

            Section.objects

            .select_related(
                "school",
                "class_obj",
                "stream",
                "medium",
                "classroom"
            )
        )

        return self.filter_queryset_by_school(
            queryset
        )