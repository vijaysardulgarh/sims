from rest_framework import serializers

from apps.accounts.permissions.models import (
    Permission
)


# ==========================================
# PERMISSION SERIALIZER
# ==========================================

class PermissionSerializer(
    serializers.ModelSerializer
):

    description = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )

    module_name = serializers.CharField(
        source="module.name",
        read_only=True
    )

    action_display = serializers.CharField(
        source="get_action_display",
        read_only=True
    )

    class Meta:

        model = Permission

        fields = [

            "id",

            "module",

            "module_name",

            "action",

            "action_display",

            "name",

            "code",

            "description",

            "is_active",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "id",

            "name",

            "code",

            "created_at",

            "updated_at",
        ]