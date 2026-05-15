from rest_framework.routers import (
    DefaultRouter
)

from apps.academics.days.views import (
    DayViewSet
)

router = DefaultRouter()

router.register(
    r"",
    DayViewSet,
    basename="day"
)

urlpatterns = router.urls