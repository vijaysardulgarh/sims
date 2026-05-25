from rest_framework import serializers

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)


# ==========================================
# LOGIN SERIALIZER
# ==========================================

class LoginSerializer(
    TokenObtainPairSerializer
):

    # ======================================
    # VALIDATE
    # ======================================

    def validate(
        self,
        attrs
    ):

        # ==================================
        # AUTHENTICATE USER
        # ==================================

        super().validate(
            attrs
        )

        user = self.user

        request = self.context.get(
            "request"
        )

        request_school = getattr(
            request,
            "school",
            None
        )

        # ==================================
        # SCHOOL VALIDATION
        # ==================================

        if (

            request_school

            and

            user.school

            and

            request_school != user.school

            and

            not user.is_superuser
        ):

            raise serializers.ValidationError(

                "Invalid school login."
            )

        # ==================================
        # GENERATE CUSTOM TOKEN
        # ==================================

        refresh = self.get_token(
            user
        )

        data = {

            "refresh": str(
                refresh
            ),

            "access": str(
                refresh.access_token
            ),
        }

        return data

    # ======================================
    # TOKEN
    # ======================================

    @classmethod
    def get_token(
        cls,
        user
    ):

        token = super().get_token(
            user
        )

        # ==================================
        # USER
        # ==================================

        token["user_id"] = user.id

        token["email"] = user.email

        token["username"] = user.username

        token["full_name"] = getattr(
            user,
            "full_name",
            ""
        )

        token["profile_photo"] = (

            user.profile_photo.url

            if user.profile_photo

            else None
        )

        # ==================================
        # SCHOOL
        # ==================================

        token["school_id"] = getattr(

            user.school,

            "id",

            None
        )

        token["school_name"] = getattr(

            user.school,

            "name",

            None
        )

        token["school_slug"] = getattr(

            user.school,

            "slug",

            None
        )

        # ==================================
        # ROLES
        # ==================================

        token["roles"] = list(

            user.user_roles.filter(

            

                is_active=True,

                is_deleted=False
            )

            .values_list(

                "role__code",

                flat=True
            )

            .distinct()
        )

        # ==================================
        # PERMISSIONS
        # ==================================

        token["permissions"] = list(

            user.user_roles.filter(

           

                is_active=True,

                is_deleted=False
            )

            .values_list(

                "role__role_permissions__permission__code",

                flat=True
            )

            .distinct()
        )

        # ==================================
        # PROFILE FLAGS
        # ==================================

        token["is_staff_profile"] = hasattr(
            user,
            "staff_profile"
        )

        token["is_student_profile"] = hasattr(
            user,
            "student_profile"
        )

        # ==================================
        # SYSTEM FLAGS
        # ==================================

        token["is_superuser"] = (
            user.is_superuser
        )

        token["is_staff"] = (
            user.is_staff
        )

        return token