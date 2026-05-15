from rest_framework.routers import (
    DefaultRouter
)

from apps.library.issues.views import (
    BookIssueViewSet
)

router = DefaultRouter()

router.register(
    r"",
    BookIssueViewSet,
    basename="book-issue"
)

urlpatterns = router.urls