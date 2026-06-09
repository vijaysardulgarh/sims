# =============================================================================
# association_members/views.py
# =============================================================================

from django.shortcuts import get_object_or_404

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.association_members.models import (
    AssociationMember
)

from apps.associations.association_members.serializers import (
    AssociationMemberSerializer
)

from apps.core.common.views import (
    BaseAPIView
)


class AssociationMemberAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        queryset = (

            AssociationMember.objects

            .filter(
                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "association",
                "academic_session",
                "staff",
                "student",
            )

            .order_by(
                "association__name",
                "member_type",
            )
        )

        association_id = request.GET.get(
            "association"
        )

        member_type = request.GET.get(
            "member_type"
        )

        if association_id:

            queryset = queryset.filter(
                association_id=association_id
            )

        if member_type:

            queryset = queryset.filter(
                member_type=member_type
            )

        serializer = (
            AssociationMemberSerializer(
                queryset,
                many=True
            )
        )

        return self.success_response(
            data=serializer.data
        )

    def post(self, request):

        serializer = (
            AssociationMemberSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(
                data=serializer.data,
                message=(
                    "Member created successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )


class AssociationMemberDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get_object(
        self,
        request,
        pk
    ):

        return get_object_or_404(

            AssociationMember.objects.filter(
                is_deleted=False
            ),

            pk=pk
        )

    def get(
        self,
        request,
        pk
    ):

        member = self.get_object(
            request,
            pk
        )

        serializer = (
            AssociationMemberSerializer(
                member
            )
        )

        return self.success_response(
            data=serializer.data
        )

    def put(
        self,
        request,
        pk
    ):

        member = self.get_object(
            request,
            pk
        )

        serializer = (
            AssociationMemberSerializer(
                member,
                data=request.data,
                partial=True
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(
                data=serializer.data,
                message=(
                    "Member updated successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )

    def delete(
        self,
        request,
        pk
    ):

        member = self.get_object(
            request,
            pk
        )

        member.is_deleted = True

        member.is_active = False

        member.save(
            update_fields=[
                "is_deleted",
                "is_active",
            ]
        )

        return self.success_response(
            message=(
                "Member deleted successfully"
            )
        )