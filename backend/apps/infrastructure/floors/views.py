from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Floor

from .serializers import (
    FloorSerializer
)


class FloorViewSet(
    ModelViewSet
):

    queryset = (

        Floor.objects
        .select_related(
            "school",
            "building"
        )
    )

    serializer_class = (
        FloorSerializer
    )