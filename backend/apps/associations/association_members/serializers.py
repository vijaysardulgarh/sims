# =============================================================================
# associations/serializers/association_member_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.association_members.models import (
    AssociationMember
)


class AssociationMemberSerializer(
    serializers.ModelSerializer
):

    association_name = serializers.CharField(
        source="association.name",
        read_only=True
    )

    staff_name = serializers.CharField(
        source="staff.name",
        read_only=True
    )

    class Meta:

        model = AssociationMember

        fields = [

            "id",

            "association",
            "association_name",

            "staff",
            "staff_name",

            "designation",
            "email",
            "phone_number",
            "image",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]