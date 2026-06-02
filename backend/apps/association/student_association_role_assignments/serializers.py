# =============================================================================
# associations/serializers/student_association_role_assignment_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.student_association_role_assignments.models import (
    StudentAssociationRoleAssignment
)


class StudentAssociationRoleAssignmentSerializer(
    serializers.ModelSerializer
):

    student_name = serializers.CharField(
        source="student.full_name_aadhar",
        read_only=True
    )

    student_srn = serializers.CharField(
        source="student.srn",
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

        model = StudentAssociationRoleAssignment

        fields = [

            "id",

            "academic_session",
            "academic_session_name",

            "student",
            "student_name",
            "student_srn",

            "role",
            "role_title",

            "association_name",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]