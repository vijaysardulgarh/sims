# =============================================================================
# associations/serializers/association_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.associations.models import Association


class AssociationSerializer(
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

    chairperson_name = serializers.CharField(
        source="chairperson.name",
        read_only=True
    )

    class Meta:

        model = Association

        fields = [

            "id",

            "school",
            "school_name",

            "academic_session",
            "academic_session_name",

            "name",
            "association_type",
            "status",

            "chairperson",
            "chairperson_name",

            "tasks",
            "documents",

            "show_on_website",
            "description",

            "slug",
            "priority",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "slug",
            "created_at",
            "updated_at",
        ]