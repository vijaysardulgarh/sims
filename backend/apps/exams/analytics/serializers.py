from rest_framework import serializers


class AnalyticsSerializer(
    serializers.Serializer
):

    total_students = serializers.IntegerField()

    total_exams = serializers.IntegerField()

    pass_percentage = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    fail_percentage = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    average_score = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    highest_score = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    lowest_score = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
    )