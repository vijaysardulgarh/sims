from rest_framework import serializers

from .models import (
    ComplianceDocument
)


class ComplianceDocumentSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = ComplianceDocument

        fields = "__all__"