from rest_framework import viewsets

from apps.academics.streams import (
    Stream
)

from apps.academics.streams.serializer import (
    StreamSerializer
)


class StreamViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Stream.objects.all()
    )

    serializer_class = (
        StreamSerializer
    )