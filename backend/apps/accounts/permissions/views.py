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

        queryset = (

            Permission.objects.filter(

                is_deleted=False
            )

            .select_related(
                "module"
            )

            .order_by(

                "module__name",

                "display_order",

                "name"
            )
        )

        # =================================
        # FILTER BY MODULE
        # =================================

        module_id = self.request.query_params.get(
            "module"
        )

        if module_id:

            queryset = queryset.filter(
                module_id=module_id
            )

        # =================================
        # FILTER BY ACTION
        # =================================

        action = self.request.query_params.get(
            "action"
        )

        if action:

            queryset = queryset.filter(
                action=action
            )

        # =================================
        # FILTER ACTIVE
        # =================================

        is_active = self.request.query_params.get(
            "is_active"
        )

        if is_active is not None:

            queryset = queryset.filter(
                is_active=is_active.lower() == "true"
            )

        return queryset

    # =====================================
    # PERFORM CREATE
    # =====================================

    def perform_create(
        self,
        serializer
    ):

        serializer.save(

            created_by=self.request.user,

            updated_by=self.request.user,
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

        return (

            Permission.objects.filter(

                is_deleted=False
            )

            .select_related(
                "module"
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
# PERMISSIONS BY MODULE API
# =========================================

class PermissionByModuleAPIView(

    generics.ListAPIView
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

        module_id = self.kwargs.get(
            "module_id"
        )

        return (

            Permission.objects.filter(

                module_id=module_id,

                is_deleted=False,

                is_active=True,
            )

            .select_related(
                "module"
            )

            .order_by(

                "display_order",

                "name"
            )
        )