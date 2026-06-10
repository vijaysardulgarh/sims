from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    ResourceAllocationViewSet,
)

router = DefaultRouter()

router.register(
    "",
    ResourceAllocationViewSet,
    basename="resource-allocations",
)

urlpatterns = router.urls