from rest_framework import serializers

from apps.accounts.user_roles.models import (
    UserRole
)


# ==========================================
# USER ROLE SERIALIZER
# ==========================================

class UserRoleSerializer(
    serializers.ModelSerializer
):

    # ======================================
    # READ ONLY FIELDS
    # ======================================

    user_email = serializers.CharField(
        source="user.email",
        read_only=True
    )

    role_name = serializers.CharField(
        source="role.name",
        read_only=True
    )

    role_code = serializers.CharField(
        source="role.code",
        read_only=True
    )

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    # ======================================
    # META
    # ======================================

    class Meta:

        model = UserRole

        fields = [

            "id",

            "school",

            "school_name",

            "user",

            "user_email",

            "role",

            "role_name",

            "role_code",

            "is_active",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "id",

            "school",

            "created_at",

            "updated_at",
        ]

    # ======================================
    # VALIDATE
    # ======================================

    def validate(
        self,
        attrs
    ):

        request = self.context.get(
            "request"
        )

        school = getattr(
            request,
            "school",
            None
        )

        user = attrs.get("user")

        role = attrs.get("role")

        queryset = UserRole.objects.filter(

            school=school,

            user=user,

            role=role,

            is_deleted=False
        )

        if self.instance:

            queryset = queryset.exclude(
                pk=self.instance.pk
            )

        if queryset.exists():

            raise serializers.ValidationError({

                "detail":
                "This role is already assigned to the user."
            })

        return attrs