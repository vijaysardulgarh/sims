from rest_framework import serializers

from apps.academics.timetables import (
    Timetable
)


class TimetableSerializer(
    serializers.ModelSerializer
):

    teacher_name = serializers.CharField(
        source="teacher.name",
        read_only=True
    )

    section_name = serializers.CharField(
        source="section.name",
        read_only=True
    )

    subject_name = serializers.CharField(
        source="class_subject.subject.name",
        read_only=True
    )

    day_name = serializers.CharField(
        source="slot.day.name",
        read_only=True
    )

    class Meta:

        model = Timetable

        fields = "__all__"