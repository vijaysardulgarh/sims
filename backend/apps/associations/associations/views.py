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
# ASSOCIATION LIST + CREATE
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

        queryset = (

            Association.objects.filter(
                is_active=True,
                is_deleted=False,
            )
        )

        if school:

            queryset = queryset.filter(
                school=school
            )

        if academic_session:

            queryset = queryset.filter(
                academic_session=academic_session
            )

        return (

            queryset

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

        data = request.data.copy()

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

        if school:

            data["school"] = school.id

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
# ASSOCIATION DETAIL + UPDATE + DELETE
# =============================================================================

class AssociationDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =========================================================================
    # OBJECT
    # =========================================================================

    def get_object(
        self,
        request,
        pk
    ):

        queryset = (

            Association.objects.filter(
                is_deleted=False
            )
        )

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

        if school:

            queryset = queryset.filter(
                school=school
            )

        if academic_session:

            queryset = queryset.filter(
                academic_session=academic_session
            )

        return get_object_or_404(

            queryset

            .select_related(
                "school",
                "academic_session",
                "chairperson",
            )

            .prefetch_related(
                "documents"
            ),

            pk=pk
        )

    # =========================================================================
    # DETAIL
    # =========================================================================

    def get(
        self,
        request,
        pk
    ):

        association = self.get_object(
            request,
            pk
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

        association = self.get_object(
            request,
            pk
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

        association = self.get_object(
            request,
            pk
        )

        association.is_deleted = True

        association.is_active = False

        association.save(

            update_fields=[
                "is_deleted",
                "is_active",
            ]
        )

        return self.success_response(

            message=(
                "Association deleted successfully"
            )
        )