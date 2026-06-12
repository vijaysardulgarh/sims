from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    PeriodDefinitionViewSet,
)

router = DefaultRouter()

router.register(
    "",
    PeriodDefinitionViewSet,
    basename="period-definitions",
)

urlpatterns = router.urls