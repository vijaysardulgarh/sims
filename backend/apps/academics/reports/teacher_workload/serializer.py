from rest_framework import serializers


class TeacherWorkloadSerializer(
    serializers.Serializer
):

    teacher_subject_assignment__teacher__name = (
        serializers.CharField()
    )

    total = serializers.IntegerField()