from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    ExamTimetableEntryViewSet,
)

router = DefaultRouter()

router.register(
    "",
    ExamTimetableEntryViewSet,
    basename="exam-timetable-entries",
)

urlpatterns = router.urls