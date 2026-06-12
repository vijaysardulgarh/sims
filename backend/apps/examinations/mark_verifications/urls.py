from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    MarkVerificationViewSet
)

router = DefaultRouter()

router.register(
    "",
    MarkVerificationViewSet,
    basename="mark-verification",
)

urlpatterns = router.urls