# =============================================================================
# groups/views/group_views.py
# =============================================================================

from django.shortcuts import get_object_or_404

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.groups.models import (
    Group
)

from apps.associations.groups.serializers import (
    GroupSerializer
)

from apps.core.common.views import (
    BaseAPIView
)


# =============================================================================
# GROUP LIST
# =============================================================================

class GroupListAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =========================================================================
    # QUERYSET
    # =========================================================================

    def get_queryset(self):

        school = getattr(
            self.request,
            "school",
            None
        )

        academic_session = getattr(
            self.request,
            "academic_session",
            None
        )

        return (

            Group.objects.filter(

                school=school,

                academic_session=academic_session,

                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "school",
                "academic_session",
                "chairperson",
            )

            .prefetch_related(
                "documents"
            )

            .order_by(
                "-priority",
                "name"
            )
        )

    # =========================================================================
    # LIST
    # =========================================================================

    def get(
        self,
        request
    ):

        serializer = (
            GroupSerializer(
                self.get_queryset(),
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

        data = request.data.copy()

        if school:

            data["school"] = (
                school.id
            )

        if academic_session:

            data["academic_session"] = (
                academic_session.id
            )

        serializer = (
            GroupSerializer(
                data=data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=(
                    "Group created successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )


# =============================================================================
# GROUP DETAIL
# =============================================================================

class GroupDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =========================================================================
    # QUERYSET
    # =========================================================================

    def get_queryset(self):

        school = getattr(
            self.request,
            "school",
            None
        )

        academic_session = getattr(
            self.request,
            "academic_session",
            None
        )

        return (

            Group.objects.filter(

                school=school,

                academic_session=academic_session,

                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "school",
                "academic_session",
                "chairperson",
            )

            .prefetch_related(
                "documents"
            )
        )

    # =========================================================================
    # DETAIL
    # =========================================================================

    def get(
        self,
        request,
        pk
    ):

        group = (
            get_object_or_404(

                self.get_queryset(),

                pk=pk
            )
        )

        serializer = (
            GroupSerializer(
                group
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

        group = (
            get_object_or_404(

                self.get_queryset(),

                pk=pk
            )
        )

        data = request.data.copy()

        serializer = (
            GroupSerializer(

                group,

                data=data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=(
                    "Group updated successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )

    # =========================================================================
    # PARTIAL UPDATE
    # =========================================================================

    def patch(
        self,
        request,
        pk
    ):

        group = (
            get_object_or_404(

                self.get_queryset(),

                pk=pk
            )
        )

        serializer = (
            GroupSerializer(

                group,

                data=request.data,

                partial=True
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=(
                    "Group updated successfully"
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

        group = (
            get_object_or_404(

                self.get_queryset(),

                pk=pk
            )
        )

        group.is_deleted = True

        group.save()

        return self.success_response(

            message=(
                "Group deleted successfully"
            )
        )