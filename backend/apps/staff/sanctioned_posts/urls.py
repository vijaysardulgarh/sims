from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    SanctionedPostViewSet
)

router = DefaultRouter()

router.register(
    "",
    SanctionedPostViewSet,
    basename="sanctioned-posts"
)

urlpatterns = router.urls