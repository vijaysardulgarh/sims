from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.accounts.permissions.models import (
    Permission
)

from apps.accounts.permissions.serializers import (
    PermissionSerializer
)


# =========================================
# PERMISSION LIST CREATE API
# =========================================

class PermissionListAPIView(

    generics.ListCreateAPIView
):

    serializer_class = (
        PermissionSerializer
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

        # =================================
        # SUPER ADMIN
        # =================================

        if self.request.user.is_superuser:

            return (

                Permission.objects.filter(

                    is_deleted=False
                )

                .order_by(

                    "module",

                    "display_order",

                    "name"
                )
            )

        # =================================
        # SCHOOL ADMIN
        # =================================

        return (

            Permission.objects.filter(

                school=getattr(

                    self.request.user,

                    "school",

                    None
                ),

                is_deleted=False
            )

            .order_by(

                "module",

                "display_order",

                "name"
            )
        )

    # =====================================
    # PERFORM CREATE
    # =====================================

    def perform_create(
        self,
        serializer
    ):

        # =================================
        # SUPER ADMIN
        # =================================

        if self.request.user.is_superuser:

            serializer.save(

                created_by=self.request.user
            )

        # =================================
        # SCHOOL ADMIN
        # =================================

        else:

            serializer.save(

                school=getattr(

                    self.request.user,

                    "school",

                    None
                ),

                created_by=self.request.user
            )


# =========================================
# PERMISSION DETAIL API
# =========================================

class PermissionDetailAPIView(

    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = (
        PermissionSerializer
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

        # =================================
        # SUPER ADMIN
        # =================================

        if self.request.user.is_superuser:

            return Permission.objects.filter(

                is_deleted=False
            )

        # =================================
        # SCHOOL ADMIN
        # =================================

        return Permission.objects.filter(

            school=getattr(

                self.request.user,

                "school",

                None
            ),

            is_deleted=False
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