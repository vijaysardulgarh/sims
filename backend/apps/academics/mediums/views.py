from apps.academics.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.mediums.models import (
    Medium
)

from apps.academics.mediums.serializers import (
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

        return self.filter_queryset_by_school(
            queryset
        )