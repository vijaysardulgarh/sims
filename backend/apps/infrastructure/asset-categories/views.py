from rest_framework.viewsets import (
    ModelViewSet
)

from .models import AssetCategory

from .serializers import (
    AssetCategorySerializer
)


class AssetCategoryViewSet(
    ModelViewSet
):

    queryset = (
        AssetCategory.objects
        .select_related("school")
    )

    serializer_class = (
        AssetCategorySerializer
    )