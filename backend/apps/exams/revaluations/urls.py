from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    RevaluationViewSet
)

router = DefaultRouter()

router.register(
    "",
    RevaluationViewSet,
    basename="revaluation",
)

urlpatterns = router.urls