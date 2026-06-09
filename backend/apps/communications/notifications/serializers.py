from rest_framework import serializers

from .models import Notification


class NotificationSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    template_name = serializers.CharField(
        source="template.name",
        read_only=True
    )

    class Meta:

        model = Notification

        fields = "__all__"

        read_only_fields = [

            "school",

            "created_at",
            "updated_at",

            "created_by",
            "updated_by",
        ]