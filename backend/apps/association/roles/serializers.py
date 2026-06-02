# =============================================================================
# associations/roles/serializers/role_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.roles.models import (
    Role
)


class RoleSerializer(
    serializers.ModelSerializer
):

    group_name = serializers.CharField(
        source="group.name",
        read_only=True
    )

    class Meta:

        model = Role

        fields = [

            "id",

            "group",
            "group_name",

            "title",
            "responsibilities",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]