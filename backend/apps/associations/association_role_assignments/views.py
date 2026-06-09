# =============================================================================
# association_role_assignments/views.py
# =============================================================================

from apps.core.common.views import (
    SchoolFilteredViewSet
)

from apps.associations.association_role_assignments.models import (
    AssociationRoleAssignment
)

from apps.associations.association_role_assignments.serializers import (
    AssociationRoleAssignmentSerializer
)


class AssociationRoleAssignmentViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        AssociationRoleAssignmentSerializer
    )

    queryset = (

        AssociationRoleAssignment.objects

        .filter(
            is_deleted=False
        )

        .select_related(

            "member",

            "member__association",

            "role",

            "academic_session",
        )
    )

    search_fields = [

        "role__title",

        "member__association__name",
    ]

    filterset_fields = [

        "role",

        "member__association",

        "is_active",
    ]

    ordering_fields = [

        "created_at",

        "role__title",
    ]

    ordering = [

        "role__title",
    ]