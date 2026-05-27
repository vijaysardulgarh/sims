# =============================================================================
# associations/serializers/association_meeting_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.association_meetings.models import (
    AssociationMeeting
)


class AssociationMeetingSerializer(
    serializers.ModelSerializer
):

    association_name = serializers.CharField(
        source="association.name",
        read_only=True
    )

    academic_session_name = serializers.CharField(
        source="academic_session.name",
        read_only=True
    )

    class Meta:

        model = AssociationMeeting

        fields = [

            "id",

            "academic_session",
            "academic_session_name",

            "association",
            "association_name",

            "meeting_date",
            "agenda",
            "location",

            "minutes_document",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]