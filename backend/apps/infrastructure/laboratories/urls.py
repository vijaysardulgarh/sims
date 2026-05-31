from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    LaboratoryViewSet
)

router = DefaultRouter()

router.register(
    "",
    LaboratoryViewSet,
    basename="laboratories"
)

urlpatterns = router.urls