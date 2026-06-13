from rest_framework import serializers

from apps.timetables.timetable_entries.models import (
    TimetableEntry
)


# =============================================================================
# GENERATE TIMETABLE
# =============================================================================

class GenerateTimetableSerializer(
    serializers.Serializer
):

    timetable = serializers.IntegerField()


# =============================================================================
# MOVE ENTRY
# =============================================================================

class MoveEntrySerializer(
    serializers.Serializer
):

    entry_id = serializers.IntegerField()

    day = serializers.CharField()

    period = serializers.IntegerField()


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


# =============================================================================
# TIMETABLE GRID
# =============================================================================

class TimetableGridSerializer(
    serializers.ModelSerializer
):

    subject_name = serializers.SerializerMethodField()

    teacher_name = serializers.SerializerMethodField()

    room_name = serializers.SerializerMethodField()

    period_number = serializers.SerializerMethodField()

    period_name = serializers.SerializerMethodField()

    class Meta:

        model = TimetableEntry

        fields = [

            "id",

            "timetable",

            "day",

            "period",

            "period_number",

            "period_name",

            "subject",

            "subject_name",

            "teacher",

            "teacher_name",

            "room",

            "room_name",

            "remarks",

        ]

        read_only_fields = fields

    def get_subject_name(
        self,
        obj
    ):

        return str(
            obj.subject
        ) if obj.subject else ""

    def get_teacher_name(
        self,
        obj
    ):

        return str(
            obj.teacher
        ) if obj.teacher else ""

    def get_room_name(
        self,
        obj
    ):

        if not hasattr(
            obj,
            "room"
        ):

            return ""

        return str(
            obj.room
        ) if obj.room else ""

    def get_period_number(
        self,
        obj
    ):

        if not obj.period:

            return None

        return getattr(
            obj.period,
            "display_order",
            None
        )

    def get_period_name(
        self,
        obj
    ):

        if not obj.period:

            return ""

        return str(
            obj.period
        )