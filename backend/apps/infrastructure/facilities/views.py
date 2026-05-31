from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Facility

from .serializers import (
    FacilitySerializer
)


class FacilityViewSet(
    ModelViewSet
):

    queryset = (
        Facility.objects
        .select_related("school")
    )

    serializer_class = (
        FacilitySerializer
    )