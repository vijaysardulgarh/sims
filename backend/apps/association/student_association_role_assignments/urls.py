# =============================================================================
# associations/urls/student_association_role_assignment_urls.py
# =============================================================================

from django.urls import path

from apps.associations.student_association_role_assignments.views import (
    StudentAssociationRoleAssignmentAPIView
)

urlpatterns = [

    path(

        "",

        StudentAssociationRoleAssignmentAPIView.as_view(),

        name="student-association-role-assignment-list"
    ),
]