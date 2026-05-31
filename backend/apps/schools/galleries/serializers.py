from rest_framework import serializers

from .models import Gallery


class GallerySerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = Gallery

        fields = "__all__"