from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Notice

from .serializers import (
    NoticeSerializer
)


class NoticeViewSet(
    ModelViewSet
):

    queryset = (
        Notice.objects
        .select_related("school")
    )

    serializer_class = (
        NoticeSerializer
    )