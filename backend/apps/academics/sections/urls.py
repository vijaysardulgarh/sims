from rest_framework.routers import (
    DefaultRouter
)

from apps.academics.sections.views import (
    SectionViewSet
)

router = DefaultRouter()

router.register(
    r"",
    SectionViewSet,
    basename="section"
)

urlpatterns = router.urls