from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    DateSheetViewSet
)

router = DefaultRouter()

router.register(
    "",
    DateSheetViewSet,
    basename="date-sheet"
)

urlpatterns = router.urls