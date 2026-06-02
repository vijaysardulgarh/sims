# =============================================================================
# meetings/serializers/meeting_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.meetings.models import (
    Meeting
)


class MeetingSerializer(
    serializers.ModelSerializer
):

    group_name = serializers.CharField(
        source="group.name",
        read_only=True
    )

    academic_session_name = serializers.CharField(
        source="academic_session.name",
        read_only=True
    )

    class Meta:

        model = Meeting

        fields = [

            "id",

            "academic_session",
            "academic_session_name",

            "group",
            "group_name",

            "meeting_date",
            "agenda",
            "location",

            "minutes_document",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]