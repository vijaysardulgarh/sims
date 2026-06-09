from apps.core.common.views import (
    SchoolFilteredViewSet
)

from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        Notification.objects
        .select_related(
            "template",
            "school"
        )
    )

    serializer_class = (
        NotificationSerializer
    )