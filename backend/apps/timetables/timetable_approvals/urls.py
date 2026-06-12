from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    TimetableApprovalViewSet,
)

router = DefaultRouter()

router.register(
    "",
    TimetableApprovalViewSet,
    basename="timetable-approvals",
)

urlpatterns = router.urls