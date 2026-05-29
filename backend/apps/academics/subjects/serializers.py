from rest_framework import serializers

from apps.academics.subjects.models import (
    Subject
)


class SubjectSerializer(
    serializers.ModelSerializer
):

    # ============================================
    # RELATED FIELDS
    # ============================================

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    # ============================================
    # META
    # ============================================

    class Meta:

        model = Subject

        fields = [

            "id",

            "school",
            "school_name",

            "name",

            "code",

            "is_language",

            "is_optional",

            "has_lab",
        ]

        read_only_fields = [

            "school"
        ]