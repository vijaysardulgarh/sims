# =============================================================================
# academics/sessions/urls.py
# =============================================================================

from rest_framework.routers import (
    DefaultRouter
)

from apps.academics.sessions.views import (
    AcademicSessionViewSet
)

router = (
    DefaultRouter()
)

router.register(
    r"",
    AcademicSessionViewSet,
    basename="academic-session"
)

urlpatterns = (
    router.urls
)