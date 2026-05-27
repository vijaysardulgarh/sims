from rest_framework import serializers

from apps.exams.models import ExamSchedule


class ExamScheduleSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = ExamSchedule

        fields = "__all__"