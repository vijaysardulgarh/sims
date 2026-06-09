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

    academic_session_name = serializers.CharField(
        source="academic_session.name",
        read_only=True
    )

    class Meta:

        model = AssociationRole

        fields = [

            "id",

            "academic_session",
            "academic_session_name",

            "association",
            "association_name",

            "title",
            "responsibilities",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]

        read_only_fields = (

            "association_name",

            "academic_session_name",

            "created_at",

            "updated_at",
        )

    def validate(self, attrs):

        association = attrs.get(
            "association",
            getattr(
                self.instance,
                "association",
                None
            )
        )

        academic_session = attrs.get(
            "academic_session",
            getattr(
                self.instance,
                "academic_session",
                None
            )
        )

        if (
            association and
            academic_session and
            association.academic_session !=
            academic_session
        ):

            raise serializers.ValidationError(

                "Association and academic session must match."
            )

        return attrs