from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Circular

from .serializers import (
    CircularSerializer
)


class CircularViewSet(
    ModelViewSet
):

    queryset = (
        Circular.objects
        .select_related("school")
    )

    serializer_class = (
        CircularSerializer
    )