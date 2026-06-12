from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TimetablePublicationViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TimetablePublicationViewSet,
    basename="timetable-publications",
)

urlpatterns = router.urls