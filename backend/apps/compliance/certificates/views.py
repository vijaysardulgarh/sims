from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Certificate

from .serializers import (
    CertificateSerializer
)


class CertificateViewSet(
    ModelViewSet
):

    queryset = (
        Certificate.objects
        .select_related("school")
    )

    serializer_class = (
        CertificateSerializer
    )