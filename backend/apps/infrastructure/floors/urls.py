from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    FloorViewSet
)

router = DefaultRouter()

router.register(
    "",
    FloorViewSet,
    basename="floors"
)

urlpatterns = router.urls