from rest_framework import serializers


class ExamDashboardSerializer(
    serializers.Serializer
):

    total_exams = serializers.IntegerField()

    active_exams = serializers.IntegerField()

    completed_exams = serializers.IntegerField()

    result_published = serializers.IntegerField()

    pending_results = serializers.IntegerField()

    total_students = serializers.IntegerField()

    pass_percentage = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    fail_percentage = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )