from rest_framework.routers import DefaultRouter

from apps.schools.schools.views import (
    SchoolViewSet
)

router = DefaultRouter()

router.register(
    "",
    SchoolViewSet,
    basename="schools"
)

urlpatterns = router.urls