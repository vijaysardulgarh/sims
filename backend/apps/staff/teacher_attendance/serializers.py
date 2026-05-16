from rest_framework import serializers

from apps.staff.models import TeacherAttendance


class TeacherAttendanceSerializer(
    serializers.ModelSerializer
):

    teacher_name = serializers.CharField(
        source="teacher.name",
        read_only=True
    )

    class Meta:

        model = TeacherAttendance

        fields = [
            "id",
            "teacher",
            "teacher_name",
            "school",
            "date",
            "present",
        ]