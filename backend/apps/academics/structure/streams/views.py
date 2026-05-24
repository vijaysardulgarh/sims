from apps.core.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.structure.streams.models import (
    Stream
)

from apps.academics.structure.streams.serializers import (
    StreamSerializer
)


class StreamViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        StreamSerializer
    )

    search_fields = [
        "name"
    ]

    ordering_fields = [
        "name"
    ]

    def get_queryset(self):

        queryset = (
            Stream.objects.all()
        )

        return self.filter_queryset_by_school(
            queryset
        )