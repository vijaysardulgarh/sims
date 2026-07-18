from rest_framework import serializers

from apps.staff.profiles.models import Staff


class StaffSerializer(serializers.ModelSerializer):

    # ============================================
    # RELATED FIELDS
    # ============================================

    school_name = serializers.CharField(
        source="school.name",
        read_only=True,
    )

    post_type_name = serializers.CharField(
        source="post_type.name",
        read_only=True,
    )

    subject_name = serializers.CharField(
        source="subject.name",
        read_only=True,
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

            # SCHOOL
            "school",
            "school_name",

            # BASIC
            "employee_id",
            "name",
            "profile_picture",
            "gender",

            # FAMILY
            "father_name",
            "mother_name",
            "spouse_name",

            # EMPLOYMENT
            "post_type",
            "post_type_name",
            "designation",
            "staff_role",
            "employment_type",
            "status",

            "subject",
            "subject_name",

            "qualification",
            "teaching_experience_years",

            "priority",

            "min_periods_per_week",
            "max_periods_per_week",

            "is_class_teacher",
            "is_house_incharge",

            # CONTACT
            "mobile_number",
            "email",
            "aadhar_number",

            # ADDRESS
            "address",
            "city",
            "state",
            "pin_code",

            # DATES
            "date_of_birth",
            "joining_date",
            "current_joining_date",
            "retirement_date",

            # OTHER
            "category",
            "bio",

            # FLAGS
            "is_active",
            "is_deleted",

            # AUDIT
            "created_at",
            "updated_at",
        ]

        read_only_fields = (
            "created_at",
            "updated_at",
        )

    # ============================================
    # VALIDATIONS
    # ============================================

    def validate(self, attrs):

        joining_date = attrs.get(
            "joining_date",
            getattr(self.instance, "joining_date", None)
        )

        current_joining_date = attrs.get(
            "current_joining_date",
            getattr(self.instance, "current_joining_date", None)
        )

        retirement_date = attrs.get(
            "retirement_date",
            getattr(self.instance, "retirement_date", None)
        )

        min_periods = attrs.get(
            "min_periods_per_week",
            getattr(self.instance, "min_periods_per_week", 0)
        )

        max_periods = attrs.get(
            "max_periods_per_week",
            getattr(self.instance, "max_periods_per_week", 0)
        )

        if (
            joining_date
            and retirement_date
            and retirement_date <= joining_date
        ):
            raise serializers.ValidationError(
                {
                    "retirement_date":
                    "Retirement date must be after joining date."
                }
            )

        if (
            joining_date
            and current_joining_date
            and current_joining_date < joining_date
        ):
            raise serializers.ValidationError(
                {
                    "current_joining_date":
                    "Current joining date cannot be earlier than joining date."
                }
            )

        if min_periods > max_periods:
            raise serializers.ValidationError(
                {
                    "min_periods_per_week":
                    "Minimum periods cannot exceed maximum periods."
                }
            )

        return attrs