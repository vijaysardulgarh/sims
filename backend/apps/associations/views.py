from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

from apps.core.utils import get_current_school
from apps.associations.models import SMCMember, Association, StaffAssociationRoleAssignment
from apps.staff.models import Staff


# =========================================
# SMC MEMBERS
# =========================================
class SMCMemberAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        smcmembers = SMCMember.objects.filter(school=school)

        data = list(smcmembers.values())

        return Response(data)


# =========================================
# NODAL STAFF
# =========================================
class NodalStaffAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        nodal_assignments = StaffAssociationRoleAssignment.objects.filter(
            role__association__type__name="Nodal",
            staff__school=school,
        ).select_related(
            "staff", "role", "role__association", "role__association__type"
        )

        staff_members = Staff.objects.filter(
            association_roles__in=nodal_assignments
        ).prefetch_related(
            Prefetch(
                "association_roles",
                queryset=nodal_assignments,
                to_attr="nodal_roles"
            )
        ).distinct()

        result = []

        for staff in staff_members:
            roles = []

            if hasattr(staff, "nodal_roles"):
                for role in staff.nodal_roles:
                    roles.append({
                        "association": role.role.association.name,
                        "role": role.role.name
                    })

            result.append({
                "id": staff.id,
                "name": staff.name,
                "roles": roles
            })

        return Response(result)


# =========================================
# COMMITTEE DETAIL
# =========================================
class CommitteeDetailAPIView(APIView):

    def get(self, request, pk):

        committee = get_object_or_404(
            Association.objects.prefetch_related("roles__assigned_staff__staff"),
            pk=pk,
            type__name="Committee"
        )

        roles = []

        for role in committee.roles.all():
            staff_list = []

            for assigned in role.assigned_staff.all():
                staff_list.append({
                    "id": assigned.staff.id,
                    "name": assigned.staff.name
                })

            roles.append({
                "role": role.name,
                "staff": staff_list
            })

        return Response({
            "id": committee.id,
            "name": committee.name,
            "roles": roles
        })


# =========================================
# STAFF ASSOCIATION ROLES
# =========================================
class StaffAssociationRolesAPIView(APIView):

    def get(self, request):

        staff_members = Staff.objects.prefetch_related(
            "association_roles__role__association__type",
            "association_roles__role__association__school"
        ).all()

        data = []

        for staff in staff_members:
            roles = []

            for r in staff.association_roles.all():
                roles.append({
                    "association": r.role.association.name,
                    "type": r.role.association.type.name,
                    "role": r.role.name
                })

            data.append({
                "id": staff.id,
                "name": staff.name,
                "roles": roles
            })

        return Response(data)


# =========================================
# STATIC COMMITTEE PAGES (NOW API FLAGS)
# =========================================
class StaticCommitteeAPIView(APIView):

    def get(self, request):
        return Response({
            "safety_committee": True,
            "grievance_committee": True,
            "icc_committee": True,
            "committee_list": True,
            "committee": True
        })