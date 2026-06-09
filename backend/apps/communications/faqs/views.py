from apps.core.common.views import (
    SchoolFilteredViewSet
)

from .models import FAQ
from .serializers import FAQSerializer


class FAQViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        FAQ.objects
        .select_related("school")
    )

    serializer_class = (
        FAQSerializer
    )