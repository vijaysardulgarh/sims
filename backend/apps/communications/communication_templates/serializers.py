from rest_framework import serializers

from .models import (
    CommunicationTemplate
)


class CommunicationTemplateSerializer(
    serializers.ModelSerializer
):

    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )

    class Meta:

        model = (
            CommunicationTemplate
        )

        fields = [

            'id',

            'category',
            'category_name',

            'name',
            'subject',
            'content',

            'is_active',

            'created_at',
            'updated_at',
        ]

        read_only_fields = [

            'created_at',
            'updated_at',
        ]