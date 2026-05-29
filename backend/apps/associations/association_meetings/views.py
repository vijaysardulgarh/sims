# =============================================================================
# associations/views/association_meeting_views.py
# =============================================================================

from django.shortcuts import get_object_or_404

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.association_meetings.models import (
    AssociationMeeting
)

from apps.associations.association_meetings.serializers import (
    AssociationMeetingSerializer
)

from apps.core.common.views import (
    BaseAPIView
)


# =============================================================================
# LIST + CREATE
# =============================================================================

class AssociationMeetingAPIView(
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

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        meetings = (

            AssociationMeeting.objects.filter(
                school=school,
                academic_session=academic_session,
                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "association",
                "minutes_document",
            )

            .order_by(
                "-meeting_date"
            )
        )

        serializer = (
            AssociationMeetingSerializer(
                meetings,
                many=True
            )
        )

        return self.success_response(
            data=serializer.data
        )

    def post(self, request):

        serializer = (
            AssociationMeetingSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(
                data=serializer.data,
                message=(
                    "Association Meeting created successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )


# =============================================================================
# DETAIL + UPDATE + DELETE
# =============================================================================

class AssociationMeetingDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, pk):

        meeting = get_object_or_404(
            AssociationMeeting,
            pk=pk,
            is_deleted=False,
        )

        serializer = (
            AssociationMeetingSerializer(
                meeting
            )
        )

        return self.success_response(
            data=serializer.data
        )

    def put(self, request, pk):

        meeting = get_object_or_404(
            AssociationMeeting,
            pk=pk,
            is_deleted=False,
        )

        serializer = (
            AssociationMeetingSerializer(
                meeting,
                data=request.data,
                partial=True
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(
                data=serializer.data,
                message=(
                    "Association Meeting updated successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )

    def delete(self, request, pk):

        meeting = get_object_or_404(
            AssociationMeeting,
            pk=pk,
            is_deleted=False,
        )

        meeting.is_deleted = True
        meeting.save()

        return self.success_response(
            message=(
                "Association Meeting deleted successfully"
            )
        )