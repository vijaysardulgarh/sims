from rest_framework import serializers

from .models import AssetCategory


class AssetCategorySerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = AssetCategory

        fields = "__all__"