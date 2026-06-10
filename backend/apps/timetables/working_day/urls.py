from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    WorkingDayViewSet,
)

router = DefaultRouter()

router.register(
    "",
    WorkingDayViewSet,
    basename="working-days",
)

urlpatterns = router.urls