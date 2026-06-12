from rest_framework.routers import (
    DefaultRouter,
)

from .views import (
    SubjectConstraintViewSet,
)

router = DefaultRouter()

router.register(
    "",
    SubjectConstraintViewSet,
    basename="subject-constraints",
)

urlpatterns = router.urls