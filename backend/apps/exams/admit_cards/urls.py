from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    AdmitCardViewSet
)

router = DefaultRouter()

router.register(
    "",
    AdmitCardViewSet,
    basename="admit-card",
)

urlpatterns = router.urls