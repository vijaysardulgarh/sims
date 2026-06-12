from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TimetableVersionViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TimetableVersionViewSet,
    basename="timetable-versions",
)

urlpatterns = router.urls