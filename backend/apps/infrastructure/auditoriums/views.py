from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Auditorium

from .serializers import (
    AuditoriumSerializer
)


class AuditoriumViewSet(
    ModelViewSet
):

    queryset = (

        Auditorium.objects
        .select_related(
            "school",
            "room"
        )
    )

    serializer_class = (
        AuditoriumSerializer
    )