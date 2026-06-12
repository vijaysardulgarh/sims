from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    GradeCalculationViewSet
)

router = DefaultRouter()

router.register(
    "",
    GradeCalculationViewSet,
    basename="grade-calculation",
)

urlpatterns = router.urls