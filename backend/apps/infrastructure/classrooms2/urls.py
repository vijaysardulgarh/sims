from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    ClassroomViewSet
)

router = DefaultRouter()

router.register(
    "",
    ClassroomViewSet,
    basename="classrooms"
)

urlpatterns = router.urls