# =============================================================================
# associations/serializers/smc_member_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.smc_members.models import (
    SMCMember
)


class SMCMemberSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    academic_session_name = serializers.CharField(
        source="academic_session.name",
        read_only=True
    )

    class Meta:

        model = SMCMember

        fields = [

            "id",

            "school",
            "school_name",

            "academic_session",
            "academic_session_name",

            "name",
            "position",

            "contact_number",
            "email",

            "priority",
            "show_on_website",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]