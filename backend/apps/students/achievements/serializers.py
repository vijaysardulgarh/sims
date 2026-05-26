from rest_framework import serializers

from apps.students.profiles.models import Achievement


class AchievementSerializer(
    serializers.ModelSerializer
):

    # =====================================
    # DISPLAY FIELDS
    # =====================================

    achievement_type_display = serializers.CharField(
        source="get_achievement_type_display",
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

        model = Achievement

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
            # ACHIEVEMENT FIELDS
            # =================================

            "student_name",

            "achievement_type",

            "achievement_type_display",

            "event_name",

            "rank",

            "reward_title",

            "date",

            "remarks",
        ]

        read_only_fields = [

            "created_at",

            "updated_at",
        ]