from rest_framework import serializers

from apps.exams.models import OnlineExam


class OnlineExamSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = OnlineExam

        fields = "__all__"