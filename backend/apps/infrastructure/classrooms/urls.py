from rest_framework.routers import (
    DefaultRouter
)

from apps.infrastructure.classrooms.views import (
    ClassroomViewSet
)

router = DefaultRouter()

router.register(
    r"",
    ClassroomViewSet,
    basename="classroom"
)

urlpatterns = router.urls