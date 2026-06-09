from apps.core.common.views import (
    SchoolFilteredViewSet
)

from .models import CommunicationTemplate
from .serializers import (
    CommunicationTemplateSerializer
)


class CommunicationTemplateViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        CommunicationTemplate.objects
        .select_related(
            "category",
            "school"
        )
    )

    serializer_class = (
        CommunicationTemplateSerializer
    )