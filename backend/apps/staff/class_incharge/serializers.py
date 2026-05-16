from rest_framework import serializers

from apps.staff.models import ClassIncharge


class ClassInchargeSerializer(
    serializers.ModelSerializer
):

    teacher_name = serializers.CharField(
        source="staff.name",
        read_only=True
    )

    section_name = serializers.CharField(
        source="section.name",
        read_only=True
    )

    class Meta:

        model = ClassIncharge

        fields = [
            "id",
            "section",
            "section_name",
            "staff",
            "teacher_name",
            "effective_from",
            "effective_to",
            "active",
        ]