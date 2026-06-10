from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    InternalAssessmentViewSet
)

router = DefaultRouter()

router.register(
    "",
    InternalAssessmentViewSet,
    basename="internal-assessment",
)

urlpatterns = router.urls