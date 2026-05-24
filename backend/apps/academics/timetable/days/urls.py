from rest_framework.routers import (
    DefaultRouter
)

from apps.academics.timetable.days.views import (
    DayViewSet
)

router = DefaultRouter()

router.register(
    r"",
    DayViewSet,
    basename="day"
)

urlpatterns = router.urls