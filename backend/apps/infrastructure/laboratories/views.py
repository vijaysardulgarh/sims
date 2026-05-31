from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Laboratory

from .serializers import (
    LaboratorySerializer
)


class LaboratoryViewSet(
    ModelViewSet
):

    queryset = (

        Laboratory.objects
        .select_related(
            "school",
            "room",
            "incharge"
        )
    )

    serializer_class = (
        LaboratorySerializer
    )