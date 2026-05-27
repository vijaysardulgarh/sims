# =============================================================================
# associations/views/student_association_role_assignment_views.py
# =============================================================================

from rest_framework.permissions import IsAuthenticated

from apps.associations.student_association_role_assignments.models import (
    StudentAssociationRoleAssignment
)

from apps.associations.student_association_role_assignments.serializers import (
    StudentAssociationRoleAssignmentSerializer
)

from apps.core.common.views import BaseAPIView


class StudentAssociationRoleAssignmentAPIView(
    BaseAPIView
):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        school = getattr(request, "school", None)

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        queryset = (

            StudentAssociationRoleAssignment.objects

            .filter(
                school=school,
                academic_session=academic_session,
                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "student",
                "role",
                "role__association",
                "academic_session",
            )

            .order_by(
                "student__full_name_aadhar"
            )
        )

        serializer = (
            StudentAssociationRoleAssignmentSerializer(
                queryset,
                many=True
            )
        )

        return self.success_response(
            data=serializer.data
        )