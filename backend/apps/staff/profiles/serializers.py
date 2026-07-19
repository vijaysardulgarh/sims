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
            "staff_role",
            "employment_type",
            "designation",
            "status",

            # SUBJECT
            "subject",
            "subject_name",

            # QUALIFICATION
            "qualification",

            # EXPERIENCE
            "teaching_experience_years",

            # CONTACT
            "mobile_number",
            "email",
            "aadhar_number",

            # ADDRESS
            "address",
            "city",
            "district",
            "state",
            "country",
            "pin_code",

            # DATES
            "date_of_birth",
            "joining_date",
            "current_joining_date",
            "retirement_date",

            # OTHER
            "category",
            "bio",

            # STATUS
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
            getattr(self.instance, "joining_date", None),
        )

        current_joining_date = attrs.get(
            "current_joining_date",
            getattr(self.instance, "current_joining_date", None),
        )

        retirement_date = attrs.get(
            "retirement_date",
            getattr(self.instance, "retirement_date", None),
        )

        mobile_number = attrs.get(
            "mobile_number",
            getattr(self.instance, "mobile_number", ""),
        )

        aadhar_number = attrs.get(
            "aadhar_number",
            getattr(self.instance, "aadhar_number", ""),
        )

        pin_code = attrs.get(
            "pin_code",
            getattr(self.instance, "pin_code", ""),
        )

        # ========================================
        # DATE VALIDATION
        # ========================================

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

        # ========================================
        # MOBILE VALIDATION
        # ========================================

        if mobile_number:

            if (
                not mobile_number.isdigit()
                or len(mobile_number) != 10
            ):
                raise serializers.ValidationError(
                    {
                        "mobile_number":
                        "Enter a valid 10-digit mobile number."
                    }
                )

        # ========================================
        # AADHAAR VALIDATION
        # ========================================

        if aadhar_number:

            if (
                not aadhar_number.isdigit()
                or len(aadhar_number) != 12
            ):
                raise serializers.ValidationError(
                    {
                        "aadhar_number":
                        "Aadhaar number must contain exactly 12 digits."
                    }
                )

        # ========================================
        # PIN CODE VALIDATION
        # ========================================

        if pin_code:

            if (
                not pin_code.isdigit()
                or len(pin_code) != 6
            ):
                raise serializers.ValidationError(
                    {
                        "pin_code":
                        "PIN code must contain exactly 6 digits."
                    }
                )

        return attrs