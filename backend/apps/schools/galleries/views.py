from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Gallery

from .serializers import (
    GallerySerializer
)


class GalleryViewSet(
    ModelViewSet
):

    queryset = (
        Gallery.objects
        .select_related("school")
    )

    serializer_class = (
        GallerySerializer
    )