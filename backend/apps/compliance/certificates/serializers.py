from rest_framework import serializers

from .models import Certificate


class CertificateSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = Certificate

        fields = "__all__"