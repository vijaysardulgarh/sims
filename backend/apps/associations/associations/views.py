# =============================================================================
# associations/views/association_views.py
# =============================================================================

from django.shortcuts import get_object_or_404

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.associations.models import (
    Association
)

from apps.associations.associations.serializers import (
    AssociationSerializer
)

from apps.core.common.views import BaseAPIView


# =============================================================================
# ASSOCIATION LIST
# =============================================================================

class AssociationListAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =========================================================================
    # QUERYSET
    # =========================================================================

    def get_queryset(self):

        school = getattr(
            self.request,
            "school",
            None
        )

        academic_session = getattr(
            self.request,
            "academic_session",
            None
        )

        return (

            Association.objects.filter(

                school=school,

                academic_session=academic_session,

                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "school",
                "academic_session",
                "chairperson",
            )

            .prefetch_related(
                "documents"
            )

            .order_by(
                "-priority",
                "name"
            )
        )

    # =========================================================================
    # LIST
    # =========================================================================

    def get(self, request):

        queryset = self.get_queryset()

        serializer = AssociationSerializer(
            queryset,
            many=True
        )

        return self.success_response(
            data=serializer.data
        )

    # =========================================================================
    # CREATE
    # =========================================================================

    def post(self, request):

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

        data = request.data.copy()

        if school:

            data["school"] = school.id

        if academic_session:

            data["academic_session"] = (
                academic_session.id
            )

        serializer = AssociationSerializer(
            data=data
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=(
                    "Association created successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )


# =============================================================================
# COMMITTEE DETAIL
# =============================================================================

class CommitteeDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =========================================================================
    # QUERYSET
    # =========================================================================

    def get_queryset(self):

        school = getattr(
            self.request,
            "school",
            None
        )

        academic_session = getattr(
            self.request,
            "academic_session",
            None
        )

        return (

            Association.objects.filter(

                school=school,

                academic_session=academic_session,

                association_type="Committee",

                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "school",
                "academic_session",
                "chairperson",
            )

            .prefetch_related(
                "documents",
                "roles__assigned_staff__staff"
            )
        )

    # =========================================================================
    # DETAIL
    # =========================================================================

    def get(self, request, pk):

        committee = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )

        roles = []

        for role in committee.roles.all():

            assigned_staff = []

            for assignment in (
                role.assigned_staff.all()
            ):

                assigned_staff.append({

                    "id":
                        assignment.staff.id,

                    "name":
                        str(assignment.staff),
                })

            roles.append({

                "role":
                    role.title,

                "staff":
                    assigned_staff,
            })

        return self.success_response(

            data={

                "id":
                    committee.id,

                "name":
                    committee.name,

                "association_type":
                    committee.association_type,

                "status":
                    committee.status,

                "slug":
                    committee.slug,

                "description":
                    committee.description,

                "tasks":
                    committee.tasks,

                "chairperson":

                    str(committee.chairperson)
                    if committee.chairperson
                    else None,

                "roles":
                    roles,
            }
        )