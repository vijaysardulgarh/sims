from django.contrib.auth.password_validation import (
    validate_password
)

from rest_framework import serializers

from apps.accounts.users.models import (
    User
)


# ==========================================
# USER SERIALIZER
# ==========================================

class UserSerializer(
    serializers.ModelSerializer
):

    # =====================================
    # PASSWORD
    # =====================================

    password = serializers.CharField(

        write_only=True,

        required=False
    )

    # =====================================
    # EXTRA READ FIELDS
    # =====================================

    full_name = serializers.ReadOnlyField()

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    roles = serializers.SerializerMethodField()

    permissions = serializers.SerializerMethodField()

    is_staff_profile = (
        serializers.SerializerMethodField()
    )

    is_student_profile = (
        serializers.SerializerMethodField()
    )

    # =====================================
    # META
    # =====================================

    class Meta:

        model = User

        fields = [

            "id",

            "school",

            "school_name",

            "email",

            "first_name",

            "last_name",

            "full_name",

            "phone",

            "profile_photo",

            "designation",

            "password",

            "is_active",

            "is_staff",

            "is_superuser",

            "is_email_verified",

            "is_phone_verified",

            "roles",

            "permissions",

            "is_staff_profile",

            "is_student_profile",
        ]

        read_only_fields = [

            "id",

            "school",

            "roles",

            "permissions",

            "is_staff_profile",

            "is_student_profile",
        ]

    # =====================================
    # VALIDATE PASSWORD
    # =====================================

    def validate_password(
        self,
        value
    ):

        validate_password(value)

        return value

    # =====================================
    # CREATE
    # =====================================

    def create(
        self,
        validated_data
    ):

        password = validated_data.pop(
            "password",
            None
        )

        request = self.context.get(
            "request"
        )

        user = User.objects.create_user(

            password=password,

            school=request.school,

            **validated_data
        )

        return user

    # =====================================
    # UPDATE
    # =====================================

    def update(

        self,

        instance,

        validated_data

    ):

        password = validated_data.pop(
            "password",
            None
        )

        for attr, value in validated_data.items():

            setattr(
                instance,
                attr,
                value
            )

        if password:

            instance.set_password(
                password
            )

        instance.updated_by = (
            self.context["request"].user
        )

        instance.save()

        return instance

    # =====================================
    # ROLES
    # =====================================

    def get_roles(
        self,
        obj
    ):

        return list(

            obj.user_roles.filter(

                school=obj.school,

                is_active=True,

                is_deleted=False

            ).values_list(

                "role__code",

                flat=True

            ).distinct()
        )

    # =====================================
    # PERMISSIONS
    # =====================================

    def get_permissions(
        self,
        obj
    ):

        return list(

            obj.user_roles.filter(

                school=obj.school,

                is_active=True,

                is_deleted=False

            ).values_list(

                "role__role_permissions__permission__code",

                flat=True

            ).distinct()
        )

    # =====================================
    # STAFF PROFILE
    # =====================================

    def get_is_staff_profile(
        self,
        obj
    ):

        return hasattr(
            obj,
            "staff_profile"
        )

    # =====================================
    # STUDENT PROFILE
    # =====================================

    def get_is_student_profile(
        self,
        obj
    ):

        return hasattr(
            obj,
            "student_profile"
        )