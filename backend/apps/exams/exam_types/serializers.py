from rest_framework import serializers

from apps.exams.models import ExamType


class ExamTypeSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = ExamType

        fields = "__all__"