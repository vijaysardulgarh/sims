from rest_framework import serializers

from apps.users.models.user_model import (
    User
)


class UserSerializer(
    serializers.ModelSerializer
):

    # =====================================
    # EXTRA WRITE FIELD
    # =====================================

    password = serializers.CharField(

        write_only=True,

        required=False
    )


    # =====================================
    # EXTRA READ FIELDS
    # =====================================

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

            "email",

            "first_name",

            "last_name",

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

        user = User.objects.create_user(

            password=password,

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
                is_active=True
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
                is_active=True
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