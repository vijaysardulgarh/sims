from rest_framework import serializers

from .models import Notification


class NotificationSerializer(
    serializers.ModelSerializer
):

    template_name = (
        serializers.CharField(
            source='template.name',
            read_only=True
        )
    )

    class Meta:

        model = Notification

        fields = '__all__'