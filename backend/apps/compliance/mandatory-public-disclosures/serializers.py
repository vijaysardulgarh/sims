from rest_framework import serializers

from .models import (
    MandatoryPublicDisclosure
)


class MandatoryPublicDisclosureSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = (
            MandatoryPublicDisclosure
        )

        fields = "__all__"