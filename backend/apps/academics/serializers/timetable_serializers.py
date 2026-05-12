from rest_framework import serializers

from apps.academics.models import (
    Day,
    TimetableSlot,
    Timetable
)

from apps.academics.models import (
    TeacherSubjectAssignment
)


# =========================================
# DAY SERIALIZER
# =========================================

class DaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Day
        fields = "__all__"


# =========================================
# TIMETABLE SLOT SERIALIZER
# =========================================

class TimetableSlotSerializer(serializers.ModelSerializer):

    day_name = serializers.CharField(
        source="day.name",
        read_only=True
    )

    class Meta:
        model = TimetableSlot
        fields = "__all__"


# =========================================
# TEACHER ASSIGNMENT SERIALIZER
# =========================================

class TeacherSubjectAssignmentSerializer(
    serializers.ModelSerializer
):

    teacher_name = serializers.CharField(
        source="teacher.name",
        read_only=True
    )

    subject_name = serializers.CharField(
        source="class_subject.subject.name",
        read_only=True
    )

    section_name = serializers.CharField(
        source="section.name",
        read_only=True
    )

    class Meta:
        model = TeacherSubjectAssignment
        fields = "__all__"


# =========================================
# TIMETABLE SERIALIZER
# =========================================

class TimetableSerializer(serializers.ModelSerializer):

    teacher_name = serializers.CharField(
        source="teacher.name",
        read_only=True
    )

    section_name = serializers.CharField(
        source="section.name",
        read_only=True
    )

    subject_name = serializers.CharField(
        source="class_subject.subject.name",
        read_only=True
    )

    day_name = serializers.CharField(
        source="slot.day.name",
        read_only=True
    )

    class Meta:
        model = Timetable
        fields = "__all__"