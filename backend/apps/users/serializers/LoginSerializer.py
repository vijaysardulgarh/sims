from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)


# ==========================================
# LOGIN SERIALIZER
# ==========================================

class LoginSerializer(
    TokenObtainPairSerializer
):

    @classmethod
    def get_token(
        cls,
        user
    ):

        token = super().get_token(
            user
        )

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