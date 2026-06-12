from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TimetableConflictViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TimetableConflictViewSet,
    basename="timetable-conflicts",
)

urlpatterns = router.urls