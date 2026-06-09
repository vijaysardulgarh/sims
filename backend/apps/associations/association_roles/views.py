# =============================================================================
# association_roles/views.py
# =============================================================================

from django.shortcuts import get_object_or_404

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
# ASSOCIATION ROLE LIST + CREATE
# =============================================================================

class AssociationRoleListAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(
        self,
        request
    ):

        return (

            AssociationRole.objects

            .filter(
                is_deleted=False
            )

            .select_related(
                "association",
                "academic_session",
            )
        )

    # =========================================================================
    # LIST
    # =========================================================================

    def get(
        self,
        request
    ):

        queryset = (

            self.get_queryset(
                request
            )

            .filter(
                is_active=True
            )

            .order_by(
                "association__name",
                "title"
            )
        )

        association_id = request.GET.get(
            "association"
        )

        if association_id:

            queryset = queryset.filter(
                association_id=
                association_id
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

    # =========================================================================
    # CREATE
    # =========================================================================

    def post(
        self,
        request
    ):

        print("\n" + "=" * 80)
        print("ASSOCIATION ROLE CREATE")
        print("=" * 80)
        print("REQUEST DATA:", request.data)

        serializer = (
            AssociationRoleSerializer(
                data=request.data
            )
        )

        is_valid = serializer.is_valid()

        print(
            "IS VALID:",
            is_valid
        )

        print(
            "ERRORS:",
            serializer.errors
        )

        if not is_valid:

            return self.error_response(
                errors=serializer.errors
            )

        role = serializer.save()

        print(
            "CREATED ROLE ID:",
            role.id
        )

        return self.success_response(

            data=serializer.data,

            message=(
                "Association Role "
                "created successfully"
            )
        )


# =============================================================================
# ASSOCIATION ROLE DETAIL + UPDATE + DELETE
# =============================================================================

class AssociationRoleDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get_object(
        self,
        request,
        pk
    ):

        return get_object_or_404(

            AssociationRole.objects

            .filter(
                is_deleted=False
            )

            .select_related(
                "association",
                "academic_session",
            ),

            pk=pk
        )

    def get(
        self,
        request,
        pk
    ):

        association_role = (
            self.get_object(
                request,
                pk
            )
        )

        serializer = (
            AssociationRoleSerializer(
                association_role
            )
        )

        return self.success_response(
            data=serializer.data
        )

    def put(
        self,
        request,
        pk
    ):

        association_role = (
            self.get_object(
                request,
                pk
            )
        )

        serializer = (
            AssociationRoleSerializer(

                association_role,

                data=request.data,

                partial=True
            )
        )

        if not serializer.is_valid():

            return self.error_response(
                errors=serializer.errors
            )

        serializer.save()

        return self.success_response(

            data=serializer.data,

            message=(
                "Association Role "
                "updated successfully"
            )
        )

    def delete(
        self,
        request,
        pk
    ):

        association_role = (
            self.get_object(
                request,
                pk
            )
        )

        association_role.is_deleted = True

        association_role.is_active = False

        association_role.save(

            update_fields=[

                "is_deleted",

                "is_active",
            ]
        )

        return self.success_response(

            message=(
                "Association Role "
                "deleted successfully"
            )
        )