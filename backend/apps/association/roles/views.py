# =============================================================================
# roles/views/role_views.py
# =============================================================================

from django.shortcuts import (
    get_object_or_404
)

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.roles.models import (
    Role
)

from apps.associations.roles.serializers import (
    RoleSerializer
)

from apps.core.common.views import (
    BaseAPIView
)


# =============================================================================
# ROLE LIST + CREATE
# =============================================================================

class RoleListAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =========================================================================
    # LIST
    # =========================================================================

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

        queryset = (

            Role.objects

            .filter(

                group__school=school,

                group__academic_session=
                academic_session,

                is_active=True,

                is_deleted=False,
            )

            .select_related(
                "group"
            )

            .order_by(
                "group__name",
                "title"
            )
        )

        serializer = (
            RoleSerializer(
                queryset,
                many=True
            )
        )

        return self.success_response(
            data=serializer.data
        )

    # =========================================================================
    # CREATE
    # =========================================================================

    def post(self, request):

        serializer = (
            RoleSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=(
                    "Role created successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )


# =============================================================================
# ROLE DETAIL + UPDATE + DELETE
# =============================================================================

class RoleDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =========================================================================
    # DETAIL
    # =========================================================================

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

        role = get_object_or_404(

            Role.objects

            .filter(

                group__school=school,

                group__academic_session=
                academic_session,

                is_active=True,

                is_deleted=False,
            )

            .select_related(
                "group"
            ),

            pk=pk
        )

        serializer = (
            RoleSerializer(
                role
            )
        )

        return self.success_response(
            data=serializer.data
        )

    # =========================================================================
    # UPDATE
    # =========================================================================

    def put(
        self,
        request,
        pk
    ):

        role = get_object_or_404(

            Role,

            pk=pk,

            is_deleted=False
        )

        serializer = (
            RoleSerializer(

                role,

                data=request.data,

                partial=True
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=(
                    "Role updated successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )

    # =========================================================================
    # DELETE
    # =========================================================================

    def delete(
        self,
        request,
        pk
    ):

        role = get_object_or_404(

            Role,

            pk=pk,

            is_deleted=False
        )

        role.is_deleted = True

        role.save()

        return self.success_response(

            message=(
                "Role deleted successfully"
            )
        )