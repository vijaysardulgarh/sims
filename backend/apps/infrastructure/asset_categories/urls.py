from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    AssetCategoryViewSet
)

router = DefaultRouter()

router.register(
    "",
    AssetCategoryViewSet,
    basename="asset-categories"
)

urlpatterns = router.urls