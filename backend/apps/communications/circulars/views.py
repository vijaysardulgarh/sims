from apps.core.common.views import (
    SchoolFilteredViewSet
)

from .models import Circular
from .serializers import CircularSerializer


class CircularViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        Circular.objects
        .select_related("school")
    )

    serializer_class = (
        CircularSerializer
    )