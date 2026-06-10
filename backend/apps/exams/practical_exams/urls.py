from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    PracticalExamViewSet
)

router = DefaultRouter()

router.register(
    "",
    PracticalExamViewSet,
    basename="practical-exam",
)

urlpatterns = router.urls