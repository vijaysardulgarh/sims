from rest_framework import serializers

from apps.exams.models import ExamNotification


class ExamNotificationSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = ExamNotification

        fields = "__all__"