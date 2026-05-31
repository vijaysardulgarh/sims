from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Affiliation

from .serializers import (
    AffiliationSerializer
)


class AffiliationViewSet(
    ModelViewSet
):

    queryset = (

        Affiliation.objects
        .select_related("school")
    )

    serializer_class = (
        AffiliationSerializer
    )