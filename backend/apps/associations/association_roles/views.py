# =============================================================================
# association_roles/views.py
# =============================================================================

from django.shortcuts import (
    get_object_or_404
)

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.association_roles.models import (
    AssociationRole
)

from apps.associations.association_roles.serializers import (
    AssociationRoleSerializer
)

from apps.core.common.views import (
    BaseAPIView
)


# =============================================================================
# ASSOCIATION ROLE LIST
# =============================================================================

class AssociationRoleListAPIView(
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

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        queryset = (

            AssociationRole.objects

            .filter(

                association__school=school,

                association__academic_session=
                academic_session,

                is_active=True,

                is_deleted=False,
            )

            .select_related(
                "association"
            )

            .order_by(
                "association__name",
                "title"
            )
        )

        serializer = (
            AssociationRoleSerializer(
                queryset,
                many=True
            )
        )

        return self.success_response(
            data=serializer.data
        )


# =============================================================================
# ASSOCIATION ROLE DETAIL
# =============================================================================

class AssociationRoleDetailAPIView(
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

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        association_role = get_object_or_404(

            AssociationRole.objects

            .filter(

                association__school=school,

                association__academic_session=
                academic_session,

                is_active=True,

                is_deleted=False,
            )

            .select_related(
                "association"
            ),

            pk=pk
        )

        serializer = (
            AssociationRoleSerializer(
                association_role
            )
        )

        return self.success_response(
            data=serializer.data
        )