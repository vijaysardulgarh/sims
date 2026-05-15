from rest_framework import serializers


class BaseReportSerializer(
    serializers.Serializer
):

    success = serializers.BooleanField(
        default=True
    )

    message = serializers.CharField(
        required=False
    )