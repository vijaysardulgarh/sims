from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    BellScheduleViewSet,
)

router = DefaultRouter()

router.register(
    "",
    BellScheduleViewSet,
    basename="bell-schedules",
)

urlpatterns = router.urls