from apps.core.common.views import (
    SchoolFilteredViewSet
)

from .models import Notice
from .serializers import NoticeSerializer


class NoticeViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        Notice.objects
        .select_related("school")
    )

    serializer_class = (
        NoticeSerializer
    )