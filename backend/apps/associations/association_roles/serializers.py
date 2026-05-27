# =============================================================================
# associations/serializers/association_role_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.association_roles.models import (
    AssociationRole
)


class AssociationRoleSerializer(
    serializers.ModelSerializer
):

    association_name = serializers.CharField(
        source="association.name",
        read_only=True
    )

    class Meta:

        model = AssociationRole

        fields = [

            "id",

            "association",
            "association_name",

            "title",
            "responsibilities",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]