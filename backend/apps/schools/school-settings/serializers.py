from rest_framework import serializers

from .models import SchoolSetting


class SchoolSettingSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = SchoolSetting

        fields = "__all__"