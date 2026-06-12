from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TeacherAvailabilityViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TeacherAvailabilityViewSet,
    basename="teacher-availabilities",
)

urlpatterns = router.urls