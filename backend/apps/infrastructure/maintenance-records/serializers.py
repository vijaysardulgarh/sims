from rest_framework import serializers

from .models import (
    MaintenanceRecord
)


class MaintenanceRecordSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(

        source="school.name",

        read_only=True
    )

    asset_name = serializers.CharField(

        source="asset.name",

        read_only=True
    )

    asset_code = serializers.CharField(

        source="asset.asset_code",

        read_only=True
    )

    class Meta:

        model = MaintenanceRecord

        fields = "__all__"