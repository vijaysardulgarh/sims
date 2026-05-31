from rest_framework import serializers

from .models import Principal


class PrincipalSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = Principal

        fields = "__all__"