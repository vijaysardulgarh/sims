from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    MarkEntryViewSet
)

router = DefaultRouter()

router.register(
    "",
    MarkEntryViewSet,
    basename="mark-entry",
)

urlpatterns = router.urls