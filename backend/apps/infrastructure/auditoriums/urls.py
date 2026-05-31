from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    AuditoriumViewSet
)

router = DefaultRouter()

router.register(
    "",
    AuditoriumViewSet,
    basename="auditoriums"
)

urlpatterns = router.urls