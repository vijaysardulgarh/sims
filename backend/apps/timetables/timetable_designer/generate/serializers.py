from rest_framework import serializers

# =============================================================================
# GENERATE TIMETABLE
# =============================================================================

class GenerateTimetableSerializer(
    serializers.Serializer
):

    timetable = serializers.IntegerField()


# =============================================================================
# COPY DAY
# =============================================================================

class CopyDaySerializer(
    serializers.Serializer
):

    timetable = serializers.IntegerField()

    source_day = serializers.CharField()

    target_day = serializers.CharField()


# =============================================================================
# COPY WEEK
# =============================================================================

class CopyWeekSerializer(
    serializers.Serializer
):

    timetable = serializers.IntegerField()    