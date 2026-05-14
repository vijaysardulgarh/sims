from apps.academics.common.base_api import (
    SchoolFilteredViewSet
)

from apps.academics.streams import (
    Stream
)

from apps.academics.streams.serializer import (
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

        return (
            self.filter_queryset_by_school(
                queryset
            )
        )