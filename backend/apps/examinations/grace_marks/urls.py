from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    GraceMarkViewSet
)

router = DefaultRouter()

router.register(
    "",
    GraceMarkViewSet,
    basename="grace-mark"
)

urlpatterns = router.urls