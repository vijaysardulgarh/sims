from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    ReportCardViewSet
)

router = DefaultRouter()

router.register(
    "",
    ReportCardViewSet,
    basename="report-card",
)

urlpatterns = router.urls