from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    CircularViewSet
)

router = DefaultRouter()

router.register(
    "",
    CircularViewSet,
    basename="circulars"
)

urlpatterns = router.urls