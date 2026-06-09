# =============================================================================
# association_role_assignments/serializers.py
# =============================================================================

from rest_framework import serializers

from apps.associations.association_role_assignments.models import (
    AssociationRoleAssignment
)


class AssociationRoleAssignmentSerializer(
    serializers.ModelSerializer
):

    association_name = serializers.CharField(
        source="member.association.name",
        read_only=True
    )

    role_title = serializers.CharField(
        source="role.title",
        read_only=True
    )

    member_name = serializers.CharField(
        source="member.member_name",
        read_only=True
    )

    academic_session_name = serializers.CharField(
        source="academic_session.name",
        read_only=True
    )

    class Meta:

        model = AssociationRoleAssignment

        fields = [

            "id",

            "academic_session",
            "academic_session_name",

            "member",
            "member_name",

            "role",
            "role_title",

            "association_name",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):

        member = attrs.get("member")

        role = attrs.get("role")

        if (

            member.association_id !=

            role.association_id

        ):

            raise serializers.ValidationError(

                "Member and role must belong "
                "to the same association."
            )

        return attrs