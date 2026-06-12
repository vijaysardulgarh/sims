from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    ImprovementExamViewSet
)

router = DefaultRouter()

router.register(
    "",
    ImprovementExamViewSet,
    basename="improvement-exam",
)

urlpatterns = router.urls