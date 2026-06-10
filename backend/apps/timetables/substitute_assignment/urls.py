from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    SubstituteAssignmentViewSet,
)

router = DefaultRouter()

router.register(
    "",
    SubstituteAssignmentViewSet,
    basename="substitute-assignments",
)

urlpatterns = router.urls