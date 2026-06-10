from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TimetableEntryViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TimetableEntryViewSet,
    basename="timetable-entries",
)

urlpatterns = router.urls