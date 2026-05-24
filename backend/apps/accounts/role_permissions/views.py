from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.core.common.views import (
    BaseAPIView
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

        return (

            RolePermission.objects

            .select_related(
                "school",
                "role",
                "permission"
            )

            .filter(

                school=self.request.school,

                is_deleted=False
            )

            .order_by(
                "role"
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

            school=self.request.school,

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

        return (

            RolePermission.objects

            .select_related(
                "school",
                "role",
                "permission"
            )

            .filter(

                school=self.request.school,

                is_deleted=False
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