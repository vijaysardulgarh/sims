from rest_framework import serializers

from apps.accounts.role_permissions.models import (
    RolePermission
)


# ==========================================
# ROLE PERMISSION SERIALIZER
# ==========================================

class RolePermissionSerializer(
    serializers.ModelSerializer
):

    # ======================================
    # ROLE FIELDS
    # ======================================

    role_name = serializers.CharField(
        source="role.name",
        read_only=True
    )

    role_code = serializers.CharField(
        source="role.code",
        read_only=True
    )

    # ======================================
    # PERMISSION FIELDS
    # ======================================

    permission_name = serializers.CharField(
        source="permission.name",
        read_only=True
    )

    permission_code = serializers.CharField(
        source="permission.code",
        read_only=True
    )

    permission_module = serializers.CharField(
        source="permission.module",
        read_only=True
    )

    # ======================================
    # SCHOOL
    # ======================================

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    # ======================================
    # META
    # ======================================

    class Meta:

        model = RolePermission

        fields = [

            "id",

            "school",
            "school_name",

            "role",
            "role_name",
            "role_code",

            "permission",
            "permission_name",
            "permission_code",
            "permission_module",

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

        role = attrs.get("role")

        permission = attrs.get(
            "permission"
        )

        queryset = (

            RolePermission.objects.filter(

                school=school,

                role=role,

                permission=permission,

                is_deleted=False
            )
        )

        if self.instance:

            queryset = queryset.exclude(
                pk=self.instance.pk
            )

        if queryset.exists():

            raise serializers.ValidationError({

                "detail":
                "Permission already assigned to this role."
            })

        return attrs