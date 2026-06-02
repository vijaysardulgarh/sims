# =============================================================================
# associations/smc_members/urls.py
# =============================================================================

from rest_framework.routers import (
    DefaultRouter
)

from apps.associations.smc.views import (
    SMCMemberViewSet
)

router = (
    DefaultRouter()
)

router.register(
    r"",
    SMCMemberViewSet,
    basename="smc-member"
)

urlpatterns = (
    router.urls
)