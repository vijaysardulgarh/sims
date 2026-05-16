from rest_framework import serializers

from apps.staff.models import Staff


class StaffSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    post_type_name = serializers.CharField(
        source="post_type.name",
        read_only=True
    )

    subject_name = serializers.CharField(
        source="subject.name",
        read_only=True
    )

    class Meta:

        model = Staff

        fields = [
            "id",
            "employee_id",
            "name",
            "school",
            "school_name",
            "post_type",
            "post_type_name",
            "staff_role",
            "employment_type",
            "subject",
            "subject_name",
            "mobile_number",
            "email",
            "gender",
            "is_active",
        ]