from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Building

from .serializers import (
    BuildingSerializer
)


class BuildingViewSet(
    ModelViewSet
):

    queryset = (

        Building.objects
        .select_related("school")
    )

    serializer_class = (
        BuildingSerializer
    )