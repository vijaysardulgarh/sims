from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Principal

from .serializers import (
    PrincipalSerializer
)


class PrincipalViewSet(
    ModelViewSet
):

    queryset = (
        Principal.objects
        .select_related("school")
    )

    serializer_class = (
        PrincipalSerializer
    )