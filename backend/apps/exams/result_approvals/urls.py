from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    ResultApprovalViewSet
)

router = DefaultRouter()

router.register(
    "",
    ResultApprovalViewSet,
    basename="result-approval",
)

urlpatterns = router.urls