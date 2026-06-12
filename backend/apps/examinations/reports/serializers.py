from rest_framework import serializers


class ReportFilterSerializer(
    serializers.Serializer
):

    exam_id = serializers.IntegerField(
        required=False,
    )

    class_id = serializers.IntegerField(
        required=False,
    )

    section_id = serializers.IntegerField(
        required=False,
    )

    subject_id = serializers.IntegerField(
        required=False,
    )