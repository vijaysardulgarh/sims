from rest_framework import serializers

from apps.staff.teacher_attendance.models import TeacherAttendance


class TeacherAttendanceSerializer(serializers.ModelSerializer):

    teacher_name = serializers.CharField(
        source="teacher.name",
        read_only=True,
    )

    employee_id = serializers.CharField(
        source="teacher.employee_id",
        read_only=True,
    )

    post_type = serializers.SerializerMethodField()

    school_name = serializers.CharField(
        source="school.name",
        read_only=True,
    )

    class Meta:

        model = TeacherAttendance

        fields = [

            "id",

            "school",
            "school_name",

            "teacher",
            "teacher_name",
            "employee_id",
            "post_type",

            "date",

            "status",

            "check_in",
            "check_out",

            "remarks",

            "created_at",
            "updated_at",

        ]

        read_only_fields = [

            "id",

            "school_name",

            "teacher_name",

            "employee_id",

            "post_type",

            "created_at",

            "updated_at",

        ]

    def get_post_type(self, obj):

        if obj.teacher.post_type:
            return obj.teacher.post_type.name

        return ""