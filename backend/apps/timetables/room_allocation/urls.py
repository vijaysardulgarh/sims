from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    RoomAllocationViewSet,
)

router = DefaultRouter()

router.register(
    "",
    RoomAllocationViewSet,
    basename="room-allocations",
)

urlpatterns = router.urls