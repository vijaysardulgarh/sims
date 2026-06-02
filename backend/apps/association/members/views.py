# =============================================================================
# members/views/member_views.py
# =============================================================================

from django.shortcuts import get_object_or_404

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.members.models import (
    Member
)

from apps.associations.members.serializers import (
    MemberSerializer
)

from apps.core.common.views import (
    BaseAPIView
)


# =============================================================================
# LIST + CREATE
# =============================================================================

class MemberAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        school = getattr(
            request,
            "school",
            None
        )

        queryset = (

            Member.objects

            .filter(
                school=school,
                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "group",
                "staff",
            )

            .order_by(
                "designation",
                "staff__name"
            )
        )

        serializer = (
            MemberSerializer(
                queryset,
                many=True
            )
        )

        return self.success_response(
            data=serializer.data
        )

    def post(self, request):

        serializer = (
            MemberSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(
                data=serializer.data,
                message="Member created successfully"
            )

        return self.error_response(
            errors=serializer.errors
        )


# =============================================================================
# DETAIL + UPDATE + DELETE
# =============================================================================

class MemberDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, pk):

        member = get_object_or_404(
            Member,
            pk=pk,
            is_deleted=False,
        )

        serializer = (
            MemberSerializer(
                member
            )
        )

        return self.success_response(
            data=serializer.data
        )

    def put(self, request, pk):

        member = get_object_or_404(
            Member,
            pk=pk,
            is_deleted=False,
        )

        serializer = (
            MemberSerializer(
                member,
                data=request.data,
                partial=True
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(
                data=serializer.data,
                message="Member updated successfully"
            )

        return self.error_response(
            errors=serializer.errors
        )

    def delete(self, request, pk):

        member = get_object_or_404(
            Member,
            pk=pk,
            is_deleted=False,
        )

        member.is_deleted = True
        member.save()

        return self.success_response(
            message="Member deleted successfully"
        )