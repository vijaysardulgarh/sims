from rest_framework.routers import (
    DefaultRouter
)

from apps.academics.structure.streams.views import (
    StreamViewSet
)

router = DefaultRouter()

router.register(
    r"",
    StreamViewSet,
    basename="stream"
)

urlpatterns = router.urls