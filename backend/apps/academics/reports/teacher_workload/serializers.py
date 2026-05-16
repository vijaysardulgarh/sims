from rest_framework import serializers


class TeacherWorkloadSerializer(
    serializers.Serializer
):

    teacher_subject_assignment__teacher__id = (
        serializers.IntegerField()
    )

    teacher_subject_assignment__teacher__name = (
        serializers.CharField()
    )

    total_periods = (
        serializers.IntegerField()
    )