from rest_framework import generics

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.accounts.users.models import (
    User
)

from apps.accounts.user_roles.models import (
    UserRole
)

from apps.core.common.views import (
    BaseAPIView
)

from apps.accounts.roles.models import (
    Role
)

from apps.accounts.permissions.models import (
    Permission
)

from apps.accounts.role_permissions.models import (
    RolePermission
)

from apps.accounts.role_permissions.serializers import (

    RolePermissionSerializer
)


# =========================================
# ROLE PERMISSION LIST CREATE API
# =========================================

class RolePermissionListCreateAPIView(

    BaseAPIView,
    generics.ListCreateAPIView
):

    serializer_class = (
        RolePermissionSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


    # =====================================
    # GET QUERYSET
    # =====================================

    def get_queryset(
        self
    ):

        queryset = (

            RolePermission.objects

            .select_related(
                "school",
                "role",
                "permission"
            )

            .filter(
                is_deleted=False
            )

            .order_by(
                "role"
            )
        )

        # =================================
        # SUPER ADMIN
        # =================================

        if self.request.user.is_superuser:

            return queryset

        # =================================
        # SCHOOL FILTER
        # =================================

        return queryset.filter(

            school=getattr(

                self.request.user,

                "school",

                None
            )
        )


    # =====================================
    # PERFORM CREATE
    # =====================================

    def perform_create(
        self,
        serializer
    ):

        serializer.save(

            school=getattr(

                self.request.user,

                "school",

                None
            ),

            created_by=self.request.user
        )


# =========================================
# ROLE PERMISSION DETAIL API
# =========================================

class RolePermissionDetailAPIView(

    BaseAPIView,
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = (
        RolePermissionSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


    # =====================================
    # GET QUERYSET
    # =====================================

    def get_queryset(
        self
    ):

        queryset = (

            RolePermission.objects

            .select_related(
                "school",
                "role",
                "permission"
            )

            .filter(
                is_deleted=False
            )
        )

        # =================================
        # SUPER ADMIN
        # =================================

        if self.request.user.is_superuser:

            return queryset

        # =================================
        # SCHOOL FILTER
        # =================================

        return queryset.filter(

            school=getattr(

                self.request.user,

                "school",

                None
            )
        )


    # =====================================
    # PERFORM UPDATE
    # =====================================

    def perform_update(
        self,
        serializer
    ):

        serializer.save(
            updated_by=self.request.user
        )


    # =====================================
    # SOFT DELETE
    # =====================================

    def perform_destroy(
        self,
        instance
    ):

        instance.is_deleted = True

        instance.updated_by = (
            self.request.user
        )

        instance.save()


# =========================================
# ROLE PERMISSIONS ASSIGN API
# =========================================

class RolePermissionsAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]


    # =====================================
    # GET ROLE PERMISSIONS
    # =====================================

    def get(
        self,
        request,
        id
    ):

        role_permissions = (

            RolePermission.objects

            .select_related(
                "permission"
            )

            .filter(

                role_id=id,

                is_deleted=False
            )
        )

        permission_codes = [

            item.permission.code

            for item in role_permissions
        ]

        return Response(
            permission_codes
        )


    # =====================================
    # ASSIGN ROLE PERMISSIONS
    # =====================================

    def post(
        self,
        request,
        id
    ):

        try:

            role = Role.objects.get(
                id=id
            )

        except Role.DoesNotExist:

            return Response(

                {
                    "detail":
                    "Role not found"
                },

                status=404
            )


        permission_codes = request.data.get(

            "permissions",

            []
        )

        print(
            "PERMISSION CODES:",
            permission_codes
        )


        # =================================
        # DELETE OLD
        # =================================

        RolePermission.objects.filter(
            role=role
        ).delete()


        # =================================
        # CREATE NEW
        # =================================

        for code in permission_codes:

            try:

                permission = Permission.objects.get(
                    code=code
                )

                RolePermission.objects.create(

                    school=role.school,

                    role=role,

                    permission=permission,

                    created_by=request.user
                )

            except Permission.DoesNotExist:

                continue


        return Response({

            "message":
            "Permissions assigned successfully"
        })


