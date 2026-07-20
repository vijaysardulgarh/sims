from rest_framework import serializers

from .models import TeacherWorkload


class TeacherWorkloadSerializer(
    serializers.ModelSerializer,
):

    teacher_name = serializers.CharField(
        source="teacher.name",
        read_only=True,
    )

    employee_id = serializers.CharField(
        source="teacher.employee_id",
        read_only=True,
    )

    class Meta:

        model = TeacherWorkload

        fields = (
            "id",
            "teacher",
            "teacher_name",
            "employee_id",
            "max_periods_per_day",
            "min_periods_per_day",
            "max_periods_per_week",
            "min_periods_per_week",
            "max_consecutive_periods",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "teacher_name",
            "employee_id",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "deleted_at",
            "deleted_by",
        )

    def validate(self, attrs):

        max_day = attrs.get(
            "max_periods_per_day",
            getattr(self.instance, "max_periods_per_day", 6),
        )

        min_day = attrs.get(
            "min_periods_per_day",
            getattr(self.instance, "min_periods_per_day", 0),
        )

        max_week = attrs.get(
            "max_periods_per_week",
            getattr(self.instance, "max_periods_per_week", 36),
        )

        min_week = attrs.get(
            "min_periods_per_week",
            getattr(self.instance, "min_periods_per_week", 0),
        )

        max_consecutive = attrs.get(
            "max_consecutive_periods",
            getattr(self.instance, "max_consecutive_periods", 3),
        )

        if min_day > max_day:
            raise serializers.ValidationError(
                {
                    "min_periods_per_day":
                        "Minimum periods per day cannot exceed maximum periods per day."
                }
            )

        if min_week > max_week:
            raise serializers.ValidationError(
                {
                    "min_periods_per_week":
                        "Minimum periods per week cannot exceed maximum periods per week."
                }
            )

        if max_consecutive > max_day:
            raise serializers.ValidationError(
                {
                    "max_consecutive_periods":
                        "Maximum consecutive periods cannot exceed maximum periods per day."
                }
            )

        return attrs