from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    ExamTimetableViewSet,
)

router = DefaultRouter()

router.register(
    "",
    ExamTimetableViewSet,
    basename="exam-timetables",
)

urlpatterns = router.urls