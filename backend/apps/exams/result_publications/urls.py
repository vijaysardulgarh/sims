from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    ResultPublicationViewSet
)

router = DefaultRouter()

router.register(
    "",
    ResultPublicationViewSet,
    basename="result-publication",
)

urlpatterns = router.urls