from django.shortcuts import (
    get_object_or_404
)

from django.db.models import (
    Prefetch
)

from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.models import (

    SMCMember,

    Association,

    StaffAssociationRoleAssignment
)

from apps.staff.profiles.models import (
    Staff
)

from apps.core.common.views import (
    BaseAPIView
)


# =========================================
# SMC MEMBERS
# =========================================

class SMCMemberAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        smc_members = (

            SMCMember.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .order_by("id")
        )

        data = list(

            smc_members.values()
        )

        return self.success_response(
            data=data
        )


# =========================================
# NODAL STAFF
# =========================================

class NodalStaffAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        nodal_assignments = (

            StaffAssociationRoleAssignment.objects

            .filter(

                role__association__type__name="Nodal",

                staff__school=school,

                is_active=True,

                is_deleted=False
            )

            .select_related(

                "staff",

                "role",

                "role__association",

                "role__association__type"
            )
        )

        staff_members = (

            Staff.objects.filter(

                school=school,

                association_roles__in=
                nodal_assignments,

                is_active=True,

                is_deleted=False
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

                for role in (
                    staff.nodal_roles
                ):

                    roles.append({

                        "association":

                            role.role
                            .association.name,

                        "role":
                            role.role.name
                    })

            result.append({

                "id":
                    staff.id,

                "name":
                    staff.name,

                "roles":
                    roles
            })

        return self.success_response(
            data=result
        )


# =========================================
# COMMITTEE DETAIL
# =========================================

class CommitteeDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        pk
    ):

        school = getattr(
            request,
            "school",
            None
        )

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        committee = get_object_or_404(

            Association.objects

            .filter(

                school=school,

                is_active=True,

                is_deleted=False,

                type__name="Committee"
            )

            .prefetch_related(
                "roles__assigned_staff__staff"
            ),

            pk=pk
        )

        roles = []

        for role in committee.roles.all():

            staff_list = []

            for assigned in (
                role.assigned_staff.all()
            ):

                staff_list.append({

                    "id":
                        assigned.staff.id,

                    "name":
                        assigned.staff.name
                })

            roles.append({

                "role":
                    role.name,

                "staff":
                    staff_list
            })

        return self.success_response(

            data={

                "id":
                    committee.id,

                "name":
                    committee.name,

                "roles":
                    roles
            }
        )


# =========================================
# STAFF ASSOCIATION ROLES
# =========================================

class StaffAssociationRolesAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        staff_members = (

            Staff.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .prefetch_related(

                "association_roles__role"
                "__association__type",

                "association_roles__role"
                "__association__school"
            )
        )

        data = []

        for staff in staff_members:

            roles = []

            for role_assignment in (
                staff.association_roles.all()
            ):

                roles.append({

                    "association":

                        role_assignment.role
                        .association.name,

                    "type":

                        role_assignment.role
                        .association.type.name,

                    "role":
                        role_assignment.role.name
                })

            data.append({

                "id":
                    staff.id,

                "name":
                    staff.name,

                "roles":
                    roles
            })

        return self.success_response(
            data=data
        )


# =========================================
# STATIC COMMITTEE FLAGS
# =========================================

class StaticCommitteeAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        return self.success_response(

            data={

                "safety_committee":
                    True,

                "grievance_committee":
                    True,

                "icc_committee":
                    True,

                "committee_list":
                    True,

                "committee":
                    True
            }
        )