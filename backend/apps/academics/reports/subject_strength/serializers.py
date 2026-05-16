from rest_framework import serializers


class SubjectStrengthSerializer(
    serializers.Serializer
):

    studentclass = serializers.CharField()

    section = serializers.CharField(
        allow_null=True,
        required=False
    )

    stream = serializers.CharField(
        allow_null=True,
        required=False
    )

    subjects = serializers.DictField(
        child=serializers.IntegerField()
    )