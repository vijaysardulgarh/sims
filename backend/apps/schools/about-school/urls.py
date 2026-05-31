from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    AboutSchoolViewSet
)

router = DefaultRouter()

router.register(
    "",
    AboutSchoolViewSet,
    basename="about-schools"
)

urlpatterns = router.urls