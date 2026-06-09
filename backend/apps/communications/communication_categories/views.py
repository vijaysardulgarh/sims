from apps.core.common.views import (
    SchoolFilteredViewSet
)

from .models import CommunicationCategory
from .serializers import (
    CommunicationCategorySerializer
)


class CommunicationCategoryViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        CommunicationCategory.objects.all()
    )

    serializer_class = (
        CommunicationCategorySerializer
    )