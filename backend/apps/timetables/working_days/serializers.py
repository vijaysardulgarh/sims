from rest_framework import serializers

from .models import WorkingDay


class WorkingDaySerializer(serializers.ModelSerializer):

    day_name = serializers.CharField(
        source="get_day_code_display",
        read_only=True,
    )

    class Meta:

        model = WorkingDay

        fields = (
            "id",
            "display_order",
            "day_code",
            "day_name",
            "is_working_day",
            "is_half_day",
            "remarks",
            "school",
            "academic_session",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "deleted_at",
            "deleted_by",
        )

        read_only_fields = (
            "id",
            "day_code",
            "day_name",
            "school",
            "academic_session",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "deleted_at",
            "deleted_by",
        )

    def validate(self, attrs):
        """
        Business validations.
        """

        is_working_day = attrs.get(
            "is_working_day",
            getattr(self.instance, "is_working_day", True),
        )

        is_half_day = attrs.get(
            "is_half_day",
            getattr(self.instance, "is_half_day", False),
        )

        if not is_working_day and is_half_day:
            raise serializers.ValidationError(
                {
                    "is_half_day": (
                        "A non-working day cannot be marked as a half day."
                    )
                }
            )

        return attrs