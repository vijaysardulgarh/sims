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

            not user.is_superuser
        ):

            has_access = (

                user.user_roles.filter(

                    school=request_school,

                    is_active=True,

                    is_deleted=False

                )

                .exists()
            )

            if not has_access:

                raise serializers.ValidationError(

                    "Invalid school login."
                )

        # ==================================
        # TOKEN
        # ==================================

        refresh = self.get_token(
            user
        )

        return {

            "refresh": str(
                refresh
            ),

            "access": str(
                refresh.access_token
            ),
        }

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
        # SCHOOLS
        # ==================================

        user_roles = (

            user.user_roles.filter(

                is_active=True,

                is_deleted=False

            )

            .select_related(
                "school",
                "role"
            )
        )

        token["schools"] = [

            {

                "id": ur.school.id,

                "name": ur.school.name,

                "slug": getattr(
                    ur.school,
                    "slug",
                    None
                ),

            }

            for ur in user_roles

            if ur.school
        ]

        # ==================================
        # ROLES
        # ==================================

        token["roles"] = list(

            user_roles

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