from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    RecognitionViewSet
)

router = DefaultRouter()

router.register(
    "",
    RecognitionViewSet,
    basename="recognitions"
)

urlpatterns = router.urls