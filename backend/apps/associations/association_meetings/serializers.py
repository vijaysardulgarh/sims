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

    minutes_document_name = serializers.CharField(
        source="minutes_document.title",
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
            "minutes_document_name",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]

        read_only_fields = (

            "created_at",

            "updated_at",

            "association_name",

            "academic_session_name",

            "minutes_document_name",
        )

    def validate(self, attrs):

        association = attrs.get(
            "association",
            getattr(self.instance, "association", None)
        )

        academic_session = attrs.get(
            "academic_session",
            getattr(self.instance, "academic_session", None)
        )

        if (
            association and
            academic_session and
            association.academic_session != academic_session
        ):

            raise serializers.ValidationError(

                "Association and academic session must match."
            )

        return attrs