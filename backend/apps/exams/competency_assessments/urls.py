from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    CompetencyAssessmentViewSet
)

router = DefaultRouter()

router.register(
    "",
    CompetencyAssessmentViewSet,
    basename=(
        "competency-assessment"
    ),
)

urlpatterns = router.urls