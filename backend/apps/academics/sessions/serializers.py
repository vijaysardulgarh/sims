# =============================================================================
# academics/sessions/serializers/academic_session_serializer.py
# =============================================================================

from datetime import date

from rest_framework import serializers

from apps.academics.sessions.models import (
    AcademicSession
)


class AcademicSessionSerializer(
    serializers.ModelSerializer
):

    status = (
        serializers.SerializerMethodField()
    )

    class Meta:

        model = (
            AcademicSession
        )

        fields = "__all__"

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

    # ==========================================
    # STATUS
    # ==========================================

    def get_status(
        self,
        obj
    ):

        today = date.today()

        if (
            obj.start_date <=
            today <=
            obj.end_date
        ):
            return "Active"

        if (
            today <
            obj.start_date
        ):
            return "Upcoming"

        return "Closed"

    # ==========================================
    # VALIDATION
    # ==========================================

    def validate(
        self,
        attrs
    ):

        start_date = attrs.get(
            "start_date"
        )

        end_date = attrs.get(
            "end_date"
        )

        if (
            start_date and
            end_date and
            end_date < start_date
        ):

            raise serializers.ValidationError(
                {
                    "end_date":
                    "End date must be greater than start date."
                }
            )

        return attrs

    # ==========================================
    # SAVE
    # ==========================================

    def create(
        self,
        validated_data
    ):

        school = (
            validated_data["school"]
        )

        if validated_data.get(
            "is_current"
        ):

            AcademicSession.objects.filter(
                school=school
            ).update(
                is_current=False
            )

        return super().create(
            validated_data
        )

    def update(
        self,
        instance,
        validated_data
    ):

        school = instance.school

        if validated_data.get(
            "is_current"
        ):

            AcademicSession.objects.filter(
                school=school
            ).exclude(
                id=instance.id
            ).update(
                is_current=False
            )

        return super().update(
            instance,
            validated_data
        )