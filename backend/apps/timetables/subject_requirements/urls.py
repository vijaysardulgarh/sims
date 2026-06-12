from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    SubjectRequirementViewSet,
)

router = DefaultRouter()

router.register(
    "",
    SubjectRequirementViewSet,
    basename="subject-requirements",
)

urlpatterns = router.urls