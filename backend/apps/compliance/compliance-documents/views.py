from rest_framework.viewsets import (
    ModelViewSet
)

from .models import (
    ComplianceDocument
)

from .serializers import (
    ComplianceDocumentSerializer
)


class ComplianceDocumentViewSet(
    ModelViewSet
):

    queryset = (

        ComplianceDocument.objects
        .select_related("school")
    )

    serializer_class = (
        ComplianceDocumentSerializer
    )