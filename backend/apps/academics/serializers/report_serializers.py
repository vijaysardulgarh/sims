from rest_framework import serializers


# =========================================
# TIMETABLE ENTRY REPORT
# =========================================

class TimetableEntryReportSerializer(
    serializers.Serializer
):

    period = serializers.IntegerField()

    teacher = serializers.CharField()

    subject = serializers.CharField()

    section = serializers.CharField(
        required=False
    )


# =========================================
# WORKLOAD SERIALIZER
# =========================================

class TeacherWorkloadSerializer(
    serializers.Serializer
):

    teacher_assignment__teacher__name = (
        serializers.CharField()
    )

    total = serializers.IntegerField()