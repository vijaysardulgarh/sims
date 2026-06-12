from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    SeatingPlanViewSet
)

router = DefaultRouter()

router.register(
    "",
    SeatingPlanViewSet,
    basename="seating-plan",
)

urlpatterns = router.urls