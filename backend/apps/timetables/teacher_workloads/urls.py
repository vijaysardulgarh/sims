from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TeacherWorkloadViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TeacherWorkloadViewSet,
    basename="teacher-workloads",
)

urlpatterns = router.urls