from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    BestOfSubjectViewSet
)

router = DefaultRouter()

router.register(
    "",
    BestOfSubjectViewSet,
    basename="best-of-subject",
)

urlpatterns = router.urls