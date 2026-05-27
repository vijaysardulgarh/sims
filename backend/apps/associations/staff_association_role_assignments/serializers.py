# =============================================================================
# associations/serializers/staff_association_role_assignment_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.staff_association_role_assignments.models import (
    StaffAssociationRoleAssignment
)


class StaffAssociationRoleAssignmentSerializer(
    serializers.ModelSerializer
):

    staff_name = serializers.CharField(
        source="staff.name",
        read_only=True
    )

    role_title = serializers.CharField(
        source="role.title",
        read_only=True
    )

    association_name = serializers.CharField(
        source="role.association.name",
        read_only=True
    )

    academic_session_name = serializers.CharField(
        source="academic_session.name",
        read_only=True
    )

    class Meta:

        model = StaffAssociationRoleAssignment

        fields = [

            "id",

            "academic_session",
            "academic_session_name",

            "staff",
            "staff_name",

            "role",
            "role_title",

            "association_name",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]