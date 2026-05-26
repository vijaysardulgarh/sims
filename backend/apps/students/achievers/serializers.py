from rest_framework import serializers

from apps.students.profiles.models import Achiever


class AchieverSerializer(
    serializers.ModelSerializer
):

    # =====================================
    # DISPLAY FIELDS
    # =====================================

    student_name = serializers.CharField(
        source="achievement.student_name",
        read_only=True,
    )

    achievement_type = serializers.CharField(
        source="achievement.get_achievement_type_display",
        read_only=True,
    )

    event_name = serializers.CharField(
        source="achievement.event_name",
        read_only=True,
    )

    percentage = serializers.FloatField(
        read_only=True,
    )

    school_name = serializers.CharField(
        source="school.name",
        read_only=True,
    )

    created_by_name = serializers.CharField(
        source="created_by.username",
        read_only=True,
    )

    updated_by_name = serializers.CharField(
        source="updated_by.username",
        read_only=True,
    )

    class Meta:

        model = Achiever

        fields = [

            # =================================
            # BASE FIELDS
            # =================================

            "id",

            "school",

            "school_name",

            "is_active",

            "is_deleted",

            "created_at",

            "updated_at",

            "created_by",

            "created_by_name",

            "updated_by",

            "updated_by_name",

            # =================================
            # ACHIEVER FIELDS
            # =================================

            "achievement",

            "student_name",

            "achievement_type",

            "event_name",

            "obtained_marks",

            "total_marks",

            "percentage",
        ]

        read_only_fields = [

            "percentage",

            "created_at",

            "updated_at",
        ]