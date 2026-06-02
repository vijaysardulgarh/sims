# =============================================================================
# meetings/views/meeting_views.py
# =============================================================================

from django.shortcuts import get_object_or_404

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.meetings.models import (
    Meeting
)

from apps.associations.meetings.serializers import (
    MeetingSerializer
)

from apps.core.common.views import (
    BaseAPIView
)


# =============================================================================
# LIST + CREATE
# =============================================================================

class MeetingAPIView(
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

            Meeting.objects.filter(
                school=school,
                academic_session=academic_session,
                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "group",
                "minutes_document",
            )

            .order_by(
                "-meeting_date"
            )
        )

        serializer = (
            MeetingSerializer(
                meetings,
                many=True
            )
        )

        return self.success_response(
            data=serializer.data
        )

    def post(self, request):

        serializer = (
            MeetingSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(
                data=serializer.data,
                message=(
                    "Meeting created successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )


# =============================================================================
# DETAIL + UPDATE + DELETE
# =============================================================================

class MeetingDetailAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, pk):

        meeting = get_object_or_404(
            Meeting,
            pk=pk,
            is_deleted=False,
        )

        serializer = (
            MeetingSerializer(
                meeting
            )
        )

        return self.success_response(
            data=serializer.data
        )

    def put(self, request, pk):

        meeting = get_object_or_404(
            Meeting,
            pk=pk,
            is_deleted=False,
        )

        serializer = (
            MeetingSerializer(
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
                    "Meeting updated successfully"
                )
            )

        return self.error_response(
            errors=serializer.errors
        )

    def delete(self, request, pk):

        meeting = get_object_or_404(
            Meeting,
            pk=pk,
            is_deleted=False,
        )

        meeting.is_deleted = True
        meeting.save()

        return self.success_response(
            message=(
                "Meeting deleted successfully"
            )
        )