from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    FeeStructureViewSet
)

router = DefaultRouter()

router.register(
    r"",
    FeeStructureViewSet,
    basename="fee-structure"
)

urlpatterns = router.urls