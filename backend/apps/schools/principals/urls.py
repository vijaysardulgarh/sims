from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    PrincipalViewSet
)

router = DefaultRouter()

router.register(
    "",
    PrincipalViewSet,
    basename="principals"
)

urlpatterns = router.urls