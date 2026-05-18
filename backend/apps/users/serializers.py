from rest_framework import serializers

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)

from .models import User


# ==========================================
# LOGIN SERIALIZER
# ==========================================

class LoginSerializer(
    TokenObtainPairSerializer
):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        token["user_id"] = user.id

        token["email"] = user.email

        token["roles"] = list(

            user.user_roles.filter(
                is_active=True
            ).values_list(
                "role__code",
                flat=True
            ).distinct()
        )

        token["permissions"] = list(

            user.user_roles.filter(
                is_active=True
            ).values_list(
                "role__role_permissions__permission__code",
                flat=True
            ).distinct()
        )

        token["is_staff_profile"] = hasattr(
            user,
            "staff_profile"
        )

        token["is_student_profile"] = hasattr(
            user,
            "student_profile"
        )

        return token


# ==========================================
# USER SERIALIZER
# ==========================================

class UserSerializer(
    serializers.ModelSerializer
):

    roles = serializers.SerializerMethodField()

    permissions = serializers.SerializerMethodField()

    is_staff_profile = (
        serializers.SerializerMethodField()
    )

    is_student_profile = (
        serializers.SerializerMethodField()
    )

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

            "roles",

            "permissions",

            "is_staff_profile",

            "is_student_profile",
        ]

    # =====================================
    # ROLES
    # =====================================

    def get_roles(self, obj):

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

    def get_permissions(self, obj):

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