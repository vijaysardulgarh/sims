from rest_framework.viewsets import (
    ModelViewSet
)

from .models import News

from .serializers import (
    NewsSerializer
)


class NewsViewSet(
    ModelViewSet
):

    queryset = (
        News.objects
        .select_related("school")
    )

    serializer_class = (
        NewsSerializer
    )