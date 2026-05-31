from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    LibraryViewSet
)

router = DefaultRouter()

router.register(
    "",
    LibraryViewSet,
    basename="libraries"
)

urlpatterns = router.urls