from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    AffiliationViewSet
)

router = DefaultRouter()

router.register(
    "",
    AffiliationViewSet,
    basename="affiliations"
)

urlpatterns = router.urls