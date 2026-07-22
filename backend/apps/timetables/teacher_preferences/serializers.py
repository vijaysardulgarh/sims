from rest_framework import serializers

from .models import TeacherPreference


class TeacherPreferenceSerializer(
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

        model = TeacherPreference

        fields = (
            "id",
            "teacher",
            "teacher_name",
            "employee_id",

            "prefer_first_period",
            "avoid_first_period",

            "prefer_last_period",
            "avoid_last_period",

            "preferred_shift",

            "maximum_free_gaps",

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

        # ----------------------------------------------------
        # THIS IS THE FIX: Bypass the unique constraint check
        # ----------------------------------------------------
        extra_kwargs = {
            "teacher": {
                "validators": []
            }
        }

    def validate(self, attrs):

        maximum_free_gaps = attrs.get(
            "maximum_free_gaps",
            0,
        )

        if maximum_free_gaps < 0:

            raise serializers.ValidationError(
                {
                    "maximum_free_gaps":
                        "Maximum free gaps cannot be negative."
                }
            )

        return attrs