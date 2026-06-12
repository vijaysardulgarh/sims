from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TimetableViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TimetableViewSet,
    basename="timetables",
)

urlpatterns = router.urls