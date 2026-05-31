from rest_framework import serializers

from .models import Asset


class AssetSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(

        source="school.name",

        read_only=True
    )

    category_name = serializers.CharField(

        source="category.name",

        read_only=True
    )

    class Meta:

        model = Asset

        fields = "__all__"