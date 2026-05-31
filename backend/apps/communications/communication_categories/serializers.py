from rest_framework import serializers

from .models import (
    CommunicationCategory
)


class CommunicationCategorySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = (
            CommunicationCategory
        )

        fields = '__all__'