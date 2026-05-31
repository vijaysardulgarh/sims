from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Playground

from .serializers import (
    PlaygroundSerializer
)


class PlaygroundViewSet(
    ModelViewSet
):

    queryset = (
        Playground.objects
        .select_related("school")
    )

    serializer_class = (
        PlaygroundSerializer
    )