# =============================================================================
# academics/sessions/serializers/academic_session_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.academics.structure.sessions.models import (
    AcademicSession
)


class AcademicSessionSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = (
            AcademicSession
        )

        fields = "__all__"

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )