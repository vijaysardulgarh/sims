from rest_framework import serializers

# =============================================================================
# PUBLISH TIMETABLE
# =============================================================================

class PublishTimetableSerializer(
    serializers.Serializer
):

    timetable = serializers.IntegerField()


# =============================================================================
# COMPARE VERSION
# =============================================================================

class CompareVersionSerializer(
    serializers.Serializer
):

    source_version = serializers.IntegerField()

    target_version = serializers.IntegerField()