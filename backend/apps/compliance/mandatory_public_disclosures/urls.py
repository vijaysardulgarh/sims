from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    MandatoryPublicDisclosureViewSet
)

router = DefaultRouter()

router.register(
    "",
    MandatoryPublicDisclosureViewSet,
    basename=(
        "mandatory-public-disclosures"
    )
)

urlpatterns = router.urls