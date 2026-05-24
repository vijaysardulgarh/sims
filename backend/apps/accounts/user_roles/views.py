from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from django.shortcuts import (
    get_object_or_404
)

from apps.core.common.views import (
    BaseAPIView
)

from apps.accounts.user_roles.models import (
    UserRole
)

from apps.accounts.user_roles.serializers import (
    UserRoleSerializer
)


# =========================================
# USER ROLE LIST CREATE API
# =========================================

class UserRoleListCreateAPIView(
    BaseAPIView,
    generics.ListCreateAPIView
):

    serializer_class = (
        UserRoleSerializer
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

            UserRole.objects

            .select_related(
                "user",
                "role",
                "school"
            )

            .filter(

                school=self.getattr(request.user, "school", None),

                is_deleted=False
            )

            .order_by("-id")
        )

    # =====================================
    # PERFORM CREATE
    # =====================================

    def perform_create(
        self,
        serializer
    ):

        serializer.save(

            school=self.getattr(request.user, "school", None),

            created_by=self.request.user
        )


# =========================================
# USER ROLE DETAIL API
# =========================================

class UserRoleDetailAPIView(
    BaseAPIView,
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = (
        UserRoleSerializer
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

            UserRole.objects

            .select_related(
                "user",
                "role",
                "school"
            )

            .filter(

                school=self.getattr(request.user, "school", None),

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