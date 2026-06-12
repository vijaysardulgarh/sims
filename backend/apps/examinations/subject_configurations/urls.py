from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    SubjectConfigurationViewSet
)

router = DefaultRouter()

router.register(
    "",
    SubjectConfigurationViewSet,
    basename="subject-configuration",
)

urlpatterns = router.urls