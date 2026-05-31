from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    ComplianceDocumentViewSet
)

router = DefaultRouter()

router.register(
    "",
    ComplianceDocumentViewSet,
    basename=(
        "compliance-documents"
    )
)

urlpatterns = router.urls