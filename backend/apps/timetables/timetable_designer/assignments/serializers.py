from rest_framework import serializers

# =============================================================================
# ASSIGN SUBJECT
# =============================================================================

class AssignSubjectSerializer(
    serializers.Serializer
):

    entry_id = serializers.IntegerField()

    subject_id = serializers.IntegerField()


# =============================================================================
# ASSIGN TEACHER
# =============================================================================

class AssignTeacherSerializer(
    serializers.Serializer
):

    entry_id = serializers.IntegerField()

    teacher_id = serializers.IntegerField()


# =============================================================================
# ASSIGN ROOM
# =============================================================================

class AssignRoomSerializer(
    serializers.Serializer
):

    entry_id = serializers.IntegerField()

    room_id = serializers.IntegerField()
