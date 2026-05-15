from rest_framework import serializers

from apps.academics.timetables.models import (
    Timetable
)


class TimetableSerializer(
    serializers.ModelSerializer
):

    teacher_name = serializers.CharField(
        source=(
            "teacher_subject_assignment."
            "teacher.name"
        ),
        read_only=True
    )

    section_name = serializers.CharField(
        source=(
            "teacher_subject_assignment."
            "section.name"
        ),
        read_only=True
    )

    subject_name = serializers.CharField(
        source=(
            "teacher_subject_assignment."
            "class_subject.subject.name"
        ),
        read_only=True
    )

    day_name = serializers.CharField(
        source="slot.day.name",
        read_only=True
    )

    period_number = serializers.IntegerField(
        source="slot.period_number",
        read_only=True
    )

    classroom_name = serializers.CharField(
        source="classroom.name",
        read_only=True
    )

    substitute_teacher_name = serializers.CharField(
        source="substitute_teacher.name",
        read_only=True
    )

    class Meta:

        model = Timetable

        fields = [

            "id",

            "teacher_subject_assignment",

            "teacher_name",

            "section_name",

            "subject_name",

            "slot",

            "day_name",

            "period_number",

            "classroom",

            "classroom_name",

            "substitute_teacher",

            "substitute_teacher_name",

            "remarks",
        ]