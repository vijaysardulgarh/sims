from rest_framework import serializers

from .models import Notice


class NoticeSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = Notice

        fields = "__all__"