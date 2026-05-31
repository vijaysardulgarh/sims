from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    PlaygroundViewSet
)

router = DefaultRouter()

router.register(
    "",
    PlaygroundViewSet,
    basename="playgrounds"
)

urlpatterns = router.urls