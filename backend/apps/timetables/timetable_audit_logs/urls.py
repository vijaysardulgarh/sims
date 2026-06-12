from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TimetableAuditLogViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TimetableAuditLogViewSet,
    basename="timetable-audit-logs",
)

urlpatterns = router.urls