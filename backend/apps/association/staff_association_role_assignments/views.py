# =============================================================================
# associations/views/staff_association_role_assignment_views.py
# =============================================================================

from django.db.models import Prefetch

from rest_framework.permissions import IsAuthenticated

from apps.staff.profiles.models import Staff

from apps.associations.staff_association_role_assignments.models import (
    StaffAssociationRoleAssignment
)

from apps.core.common.views import BaseAPIView


# =============================================================================
# NODAL STAFF
# =============================================================================

class NodalStaffAPIView(BaseAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        school = getattr(
            request,
            "school",
            None
        )

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        nodal_assignments = (

            StaffAssociationRoleAssignment.objects

            .filter(

                academic_session=academic_session,

                role__association__association_type="Nodal",

                staff__school=school,

                is_active=True,

                is_deleted=False,
            )

            .select_related(

                "staff",

                "role",

                "role__association",
            )
        )

        staff_members = (

            Staff.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False,
            )

            .prefetch_related(

                Prefetch(

                    "association_roles",

                    queryset=nodal_assignments,

                    to_attr="nodal_roles"
                )
            )

            .distinct()
        )

        result = []

        for staff in staff_members:

            roles = []

            if hasattr(
                staff,
                "nodal_roles"
            ):

                for assignment in (
                    staff.nodal_roles
                ):

                    roles.append({

                        "association":

                            assignment.role
                            .association.name,

                        "role":

                            assignment.role.title,
                    })

            result.append({

                "id":
                    staff.id,

                "name":
                    staff.name,

                "roles":
                    roles,
            })

        return self.success_response(
            data=result
        )


# =============================================================================
# STAFF ASSOCIATION ROLES
# =============================================================================

class StaffAssociationRolesAPIView(
    BaseAPIView
):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        school = getattr(
            request,
            "school",
            None
        )

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        role_assignments = (

            StaffAssociationRoleAssignment.objects

            .filter(

                academic_session=academic_session,

                staff__school=school,

                is_active=True,

                is_deleted=False,
            )

            .select_related(

                "staff",

                "role",

                "role__association",
            )
        )

        staff_members = (

            Staff.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False,
            )

            .prefetch_related(

                Prefetch(

                    "association_roles",

                    queryset=role_assignments,

                    to_attr="filtered_roles"
                )
            )
        )

        data = []

        for staff in staff_members:

            roles = []

            if hasattr(
                staff,
                "filtered_roles"
            ):

                for assignment in (
                    staff.filtered_roles
                ):

                    roles.append({

                        "association":

                            assignment.role
                            .association.name,

                        "association_type":

                            assignment.role
                            .association.association_type,

                        "role":

                            assignment.role.title,
                    })

            data.append({

                "id":
                    staff.id,

                "name":
                    staff.name,

                "roles":
                    roles,
            })

        return self.success_response(
            data=data
        )