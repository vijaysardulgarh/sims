from rest_framework import serializers

from apps.academics.teacher_subject_assignments.models import (
    TeacherSubjectAssignment
)


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

        fields = [

            "id",

            "teacher",
            "teacher_name",

            "section",
            "section_name",

            "class_subject",
            "subject_name",
        ]