from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    BranchViewSet
)

router = DefaultRouter()

router.register(
    "",
    BranchViewSet,
    basename="branches"
)

urlpatterns = router.urls