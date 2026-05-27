# =============================================================================
# associations/urls/staff_association_role_assignment_urls.py
# =============================================================================

from django.urls import path

from apps.associations.staff_association_role_assignments.views import (

    NodalStaffAPIView,

    StaffAssociationRolesAPIView,
)

urlpatterns = [

    path(

        "nodal/",

        NodalStaffAPIView.as_view(),

        name="nodal-staff"
    ),

    path(

        "association-roles/",

        StaffAssociationRolesAPIView.as_view(),

        name="staff-association-roles"
    ),
]