from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    GalleryViewSet
)

router = DefaultRouter()

router.register(
    "",
    GalleryViewSet,
    basename="galleries"
)

urlpatterns = router.urls