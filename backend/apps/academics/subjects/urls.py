from rest_framework.routers import (
    DefaultRouter
)

from apps.academics.subjects.views import (
    SubjectViewSet
)

router = DefaultRouter()

router.register(
    r"",
    SubjectViewSet,
    basename="subject"
)

urlpatterns = router.urls