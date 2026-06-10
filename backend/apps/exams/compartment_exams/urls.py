from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    CompartmentExamViewSet
)

router = DefaultRouter()

router.register(
    "",
    CompartmentExamViewSet,
    basename="compartment-exam",
)

urlpatterns = router.urls