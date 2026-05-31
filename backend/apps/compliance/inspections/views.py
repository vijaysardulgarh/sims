from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Inspection

from .serializers import (
    InspectionSerializer
)


class InspectionViewSet(
    ModelViewSet
):

    queryset = (
        Inspection.objects
        .select_related("school")
    )

    serializer_class = (
        InspectionSerializer
    )