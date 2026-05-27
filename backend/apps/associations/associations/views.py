# =============================================================================
# associations/views/association_views.py
# =============================================================================

from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated

from apps.associations.associations.models import Association
from apps.core.common.views import BaseAPIView


class AssociationListAPIView(BaseAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        school = getattr(request, "school", None)

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        queryset = (

            Association.objects.filter(
                school=school,
                academic_session=academic_session,
                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "chairperson",
                "academic_session",
            )

            .order_by(
                "priority",
                "name"
            )
        )

        data = []

        for association in queryset:

            data.append({

                "id":
                    association.id,

                "name":
                    association.name,

                "association_type":
                    association.association_type,

                "chairperson":

                    association.chairperson.name
                    if association.chairperson
                    else None,

                "status":
                    association.status,

                "slug":
                    association.slug,
            })

        return self.success_response(data=data)


class CommitteeDetailAPIView(BaseAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        school = getattr(request, "school", None)

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        committee = get_object_or_404(

            Association.objects.filter(
                school=school,
                academic_session=academic_session,
                association_type="Committee",
                is_active=True,
                is_deleted=False,
            )

            .prefetch_related(
                "roles__assigned_staff__staff"
            ),

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
                        assignment.staff.name,
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

                "roles":
                    roles,
            }
        )