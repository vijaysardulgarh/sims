from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TeacherPreferenceViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TeacherPreferenceViewSet,
    basename="teacher-preferences",
)

urlpatterns = router.urls