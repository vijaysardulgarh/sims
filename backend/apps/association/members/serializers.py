# =============================================================================
# associations/serializers/member_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.members.models import (
    Member
)


class MemberSerializer(
    serializers.ModelSerializer
):

    group_name = serializers.CharField(
        source="group.name",
        read_only=True
    )

    staff_name = serializers.CharField(
        source="staff.name",
        read_only=True
    )

    class Meta:

        model = Member

        fields = [

            "id",

            "group",
            "group_name",

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