from apps.academics.common.base_api import (
    SchoolFilteredViewSet
)

from apps.academics.mediums import (
    Medium
)

from apps.academics.mediums.serializer import (
    MediumSerializer
)


class MediumViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        MediumSerializer
    )

    search_fields = [
        "name"
    ]

    ordering_fields = [
        "name"
    ]

    def get_queryset(self):

        queryset = (
            Medium.objects.all()
        )

        return (
            self.filter_queryset_by_school(
                queryset
            )
        )