from rest_framework import serializers

from apps.staff.profiles.models import Staff


class StaffSerializer(serializers.ModelSerializer):

    # ============================================
    # RELATED FIELDS
    # ============================================

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

    # ============================================
    # META
    # ============================================

    class Meta:

        model = Staff

        fields = [

            # SYSTEM
            "id",

            # USER
            "user",

            # BASIC
            "employee_id",
            "name",
            "profile_picture",
            "gender",

            # SCHOOL
            "school",
            "school_name",

            # EMPLOYMENT
            "post_type",
            "post_type_name",
            "staff_role",
            "employment_type",
            "subject",
            "subject_name",

            # CONTACT
            "mobile_number",
            "email",

            # FAMILY
            "father_name",
            "mother_name",
            "spouse_name",

            # IDENTITY
            "aadhar_number",

            # DATES
            "date_of_birth",
            "joining_date",
            "current_joining_date",
            "retirement_date",

            # OTHER
            "qualification",
            "priority",
            "max_periods_per_week",
            "category",
            "bio",

            # STATUS
            "is_active",

            # AUDIT
            "created_at",
            "updated_at",
        ]

        read_only_fields = (
            "created_at",
            "updated_at",
        )