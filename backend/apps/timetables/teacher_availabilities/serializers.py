from rest_framework import serializers

from apps.staff.profiles.models import Staff


class TeacherAvailabilityTeacherSerializer(serializers.ModelSerializer):

    teacher_name = serializers.CharField(
        source="name",
        read_only=True,
    )

    class Meta:

        model = Staff

        fields = [
            "id",
            "employee_id",
            "teacher_name",
        ]