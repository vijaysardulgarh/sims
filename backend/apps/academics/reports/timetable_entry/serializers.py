from rest_framework import serializers


# =========================================
# TIMETABLE ENTRY REPORT SERIALIZER
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

    classroom = serializers.CharField(
        required=False
    )

    day = serializers.CharField(
        required=False
    )