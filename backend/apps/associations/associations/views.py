# =============================================================================
# associations/views/association_views.py
# =============================================================================

from django.shortcuts import get_object_or_404

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.associations.models import (
    Association
)

from apps.associations.associations.serializers import (
    AssociationSerializer
)

from apps.core.common.views import (
    BaseAPIView
)


# =============================================================================
# ASSOCIATION LIST
# =============================================================================

class AssociationListAPIView(
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

            Association.objects.filter(

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
            AssociationSerializer(
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
            AssociationSerializer(
                data=data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=(
                    "Association created successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )


# =============================================================================
# ASSOCIATION DETAIL
# =============================================================================

class AssociationDetailAPIView(
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

            Association.objects.filter(

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

        association = (
            get_object_or_404(

                self.get_queryset(),

                pk=pk
            )
        )

        serializer = (
            AssociationSerializer(
                association
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

        association = (
            get_object_or_404(

                self.get_queryset(),

                pk=pk
            )
        )

        data = request.data.copy()

        serializer = (
            AssociationSerializer(

                association,

                data=data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=(
                    "Association updated successfully"
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

        association = (
            get_object_or_404(

                self.get_queryset(),

                pk=pk
            )
        )

        serializer = (
            AssociationSerializer(

                association,

                data=request.data,

                partial=True
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=(
                    "Association updated successfully"
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

        association = (
            get_object_or_404(

                self.get_queryset(),

                pk=pk
            )
        )

        association.is_deleted = True

        association.save()

        return self.success_response(

            message=(
                "Association deleted successfully"
            )
        )