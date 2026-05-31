from rest_framework import serializers

from .models import News


class NewsSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = News

        fields = "__all__"