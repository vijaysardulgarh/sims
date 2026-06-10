from rest_framework import serializers

from .models import ExamTimetable


class ExamTimetableSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = ExamTimetable

        fields = "__all__"

        read_only_fields = (
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "deleted_at",
            "deleted_by",
            "published_at",
            "published_by",
        )