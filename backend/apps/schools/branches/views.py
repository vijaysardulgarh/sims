from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.core.common.views import (
    BaseAPIView
)

from apps.schools.branches.models import (
    Branch
)

from apps.schools.branches.serializers import (
    BranchSerializer
)


# =========================================
# BRANCH LIST CREATE API
# =========================================

class BranchListCreateAPIView(

    BaseAPIView,
    generics.ListCreateAPIView
):

    serializer_class = (
        BranchSerializer
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

            Branch.objects.filter(

                school=self.getattr(request.user, "school", None),

                is_deleted=False
            )

            .select_related(
                "school",
                "created_by",
                "updated_by"
            )

            .order_by("name")
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

            created_by=self.request.user,

            updated_by=self.request.user
        )


# =========================================
# BRANCH DETAIL API
# =========================================

class BranchDetailAPIView(

    BaseAPIView,
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = (
        BranchSerializer
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

            Branch.objects.filter(

                school=self.getattr(request.user, "school", None),

                is_deleted=False
            )

            .select_related(
                "school",
                "created_by",
                "updated_by"
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