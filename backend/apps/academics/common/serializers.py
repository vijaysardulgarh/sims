from rest_framework import serializers


# =========================================
# BASE REPORT SERIALIZER
# =========================================

class BaseReportSerializer(
    serializers.Serializer
):

    success = serializers.BooleanField(
        default=True
    )

    message = serializers.CharField(
        required=False,
        allow_blank=True
    )

    data = serializers.JSONField(
        required=False
    )