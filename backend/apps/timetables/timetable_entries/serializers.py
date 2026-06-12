from rest_framework import serializers

from .models import (
    TimetableEntry,
)


class TimetableEntrySerializer(
    serializers.ModelSerializer
):

    timetable_name = serializers.CharField(
        source="timetable.name",
        read_only=True,
    )

    period_name = serializers.CharField(
        source="period.name",
        read_only=True,
    )

    subject_name = serializers.CharField(
        source="subject.name",
        read_only=True,
    )

    teacher_name = serializers.SerializerMethodField()

    class Meta:

        model = (
            TimetableEntry
        )

        fields = [

            "id",

            "timetable",
            "timetable_name",

            "day",

            "period",
            "period_name",

            "subject",
            "subject_name",

            "teacher",
            "teacher_name",

            "remarks",

            "created_at",
            "updated_at",

        ]

        read_only_fields = (

            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "deleted_at",
            "deleted_by",

            "timetable_name",
            "period_name",
            "subject_name",
            "teacher_name",

        )

    def get_teacher_name(
        self,
        obj
    ):

        return str(
            obj.teacher
        )