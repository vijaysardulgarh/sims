from rest_framework import status

from rest_framework.response import (
    Response
)

from rest_framework.permissions import (
    IsAuthenticated
)

from django.shortcuts import (
    get_object_or_404
)

from apps.core.common.views import (
    BaseAPIView
)

from apps.accounts.roles.models import (
    Role
)

from apps.accounts.roles.serializers import (
    RoleSerializer
)


# ==========================================
# ROLE LIST CREATE API VIEW
# ==========================================

class RoleListCreateAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # ======================================
    # GET ALL ROLES
    # ======================================

    def get(
        self,
        request
    ):

        roles = (

            Role.objects.filter(

                school=request.school,

                is_deleted=False

            )

            .order_by("id")
        )

        serializer = RoleSerializer(

            roles,

            many=True
        )

        return self.success_response(

            data=serializer.data,

            message="Roles fetched successfully",

            status_code=status.HTTP_200_OK
        )

    # ======================================
    # CREATE ROLE
    # ======================================

    def post(
        self,
        request
    ):

        serializer = RoleSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(

                school=request.school,

                created_by=request.user
            )

            return self.success_response(

                data=serializer.data,

                message="Role created successfully",

                status_code=status.HTTP_201_CREATED
            )

        return self.error_response(

            errors=serializer.errors,

            message="Validation failed",

            status_code=status.HTTP_400_BAD_REQUEST
        )


# ==========================================
# ROLE DETAIL API VIEW
# ==========================================

class RoleDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # ======================================
    # GET OBJECT
    # ======================================

    def get_object(
        self,
        request,
        pk
    ):

        return get_object_or_404(

            Role,

            pk=pk,

            school=request.school,

            is_deleted=False
        )

    # ======================================
    # GET SINGLE ROLE
    # ======================================

    def get(
        self,
        request,
        pk
    ):

        role = self.get_object(

            request,

            pk
        )

        serializer = RoleSerializer(
            role
        )

        return self.success_response(

            data=serializer.data,

            message="Role fetched successfully",

            status_code=status.HTTP_200_OK
        )

    # ======================================
    # UPDATE ROLE
    # ======================================

    def patch(
        self,
        request,
        pk
    ):

        role = self.get_object(

            request,

            pk
        )

        serializer = RoleSerializer(

            role,

            data=request.data,

            partial=True
        )

        if serializer.is_valid():

            serializer.save(
                updated_by=request.user
            )

            return self.success_response(

                data=serializer.data,

                message="Role updated successfully",

                status_code=status.HTTP_200_OK
            )

        return self.error_response(

            errors=serializer.errors,

            message="Validation failed",

            status_code=status.HTTP_400_BAD_REQUEST
        )

    # ======================================
    # DELETE ROLE
    # ======================================

    def delete(
        self,
        request,
        pk
    ):

        role = self.get_object(

            request,

            pk
        )

        # ==================================
        # PREVENT SYSTEM ROLE DELETE
        # ==================================

        if role.is_system_role:

            return self.error_response(

                message="System roles cannot be deleted",

                status_code=status.HTTP_400_BAD_REQUEST
            )

        # ==================================
        # SOFT DELETE
        # ==================================

        role.is_deleted = True

        role.updated_by = request.user

        role.save()

        return self.success_response(

            message="Role deleted successfully",

            status_code=status.HTTP_200_OK
        )