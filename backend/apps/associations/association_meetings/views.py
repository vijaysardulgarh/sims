# =============================================================================
# associations/views/association_meeting_views.py
# =============================================================================

from rest_framework.permissions import IsAuthenticated

from apps.associations.association_meetings.models import (
    AssociationMeeting
)

from apps.core.common.views import BaseAPIView


class AssociationMeetingAPIView(BaseAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        school = getattr(request, "school", None)

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

            .order_by("-meeting_date")
        )

        data = []

        for meeting in meetings:

            data.append({

                "id":
                    meeting.id,

                "association":
                    meeting.association.name,

                "meeting_date":
                    meeting.meeting_date,

                "location":
                    meeting.location,

                "agenda":
                    meeting.agenda,
            })

        return self.success_response(data=data)