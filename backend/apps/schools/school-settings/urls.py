from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    SchoolSettingViewSet
)

router = DefaultRouter()

router.register(
    "",
    SchoolSettingViewSet,
    basename="school-settings"
)

urlpatterns = router.urls