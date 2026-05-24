from rest_framework import serializers

from apps.accounts.roles.models import (
    Role
)


# =========================================
# ROLE SERIALIZER
# =========================================

class RoleSerializer(
    serializers.ModelSerializer
):

    description = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )

    class Meta:

        model = Role

        fields = [

            "id",

            "name",

            "code",

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