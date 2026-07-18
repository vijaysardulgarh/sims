from rest_framework import serializers

# =============================================================================
# MOVE ENTRY
# =============================================================================

class MoveEntrySerializer(
    serializers.Serializer
):

    entry_id = serializers.IntegerField()

    day = serializers.CharField()

    period = serializers.IntegerField()