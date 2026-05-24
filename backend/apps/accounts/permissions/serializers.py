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

    class Meta:

        model = Permission

        fields = [

            "id",

            "name",

            "code",

            "module",

            "description",

            "is_active",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "id",

            "created_at",

            "updated_at",
        ]

    # ======================================
    # VALIDATE CODE
    # ======================================

    def validate_code(
        self,
        value
    ):

        return value.upper()