# =============================================================================
# associations/serializers/extracurricular_activity_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.extracurricular_activities.models import (
    ExtracurricularActivity
)


class ExtracurricularActivitySerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    academic_session_name = serializers.CharField(
        source="academic_session.name",
        read_only=True
    )

    coordinator_name = serializers.CharField(
        source="coordinator.name",
        read_only=True
    )

    participants_count = serializers.SerializerMethodField()

    class Meta:

        model = ExtracurricularActivity

        fields = [

            "id",

            "school",
            "school_name",

            "academic_session",
            "academic_session_name",

            "name",
            "description",

            "category",
            "status",

            "start_date",
            "end_date",

            "location",

            "coordinator",
            "coordinator_name",

            "participants",
            "participants_count",

            "cost",
            "capacity",

            "priority",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]

    def get_participants_count(
        self,
        obj
    ):

        return obj.participants.count()