from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    RankSystemViewSet
)

router = DefaultRouter()

router.register(
    "",
    RankSystemViewSet,
    basename="rank-system",
)

urlpatterns = router.urls