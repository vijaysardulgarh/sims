from apps.core.common.views import (
    SchoolFilteredViewSet
)

from .models import Event

from .serializers import (
    EventSerializer
)


class EventViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        Event.objects
        .select_related("school")
    )

    serializer_class = (
        EventSerializer
    )