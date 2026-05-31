from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Room

from .serializers import (
    RoomSerializer
)


class RoomViewSet(
    ModelViewSet
):

    queryset = (
        Room.objects
        .select_related(
            "school",
            "building",
            "floor"
        )
    )

    serializer_class = (
        RoomSerializer
    )