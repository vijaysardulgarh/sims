from apps.core.common.views import (
    SchoolFilteredViewSet
)

from .models import News
from .serializers import NewsSerializer


class NewsViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        News.objects
        .select_related("school")
    )

    serializer_class = (
        NewsSerializer
    )