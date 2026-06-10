from rest_framework.routers import (
    DefaultRouter
)

from apps.academics.timetable.timetable_slots.views import (
    TimetableSlotViewSet
)

router = DefaultRouter()

router.register(
    r"",
    TimetableSlotViewSet,
    basename="timetable-slot"
)

urlpatterns = router.urls