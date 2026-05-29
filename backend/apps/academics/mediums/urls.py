from rest_framework.routers import (
    DefaultRouter
)

from apps.academics.mediums.views import (
    MediumViewSet
)

router = DefaultRouter()

router.register(
    r"",
    MediumViewSet,
    basename="medium"
)

urlpatterns = router.urls