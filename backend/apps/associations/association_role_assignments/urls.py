# =============================================================================
# association_role_assignments/urls.py
# =============================================================================

from rest_framework.routers import (
    DefaultRouter
)

from apps.associations.association_role_assignments.views import (
    AssociationRoleAssignmentViewSet
)

router = (
    DefaultRouter()
)

router.register(

    r"",

    AssociationRoleAssignmentViewSet,

    basename="association-role-assignment"
)

urlpatterns = (
    router.urls
)