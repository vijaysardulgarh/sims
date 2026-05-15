from rest_framework import serializers

from apps.academics.models import (
    Subject,
    ClassSubject
)


# =========================================
# SUBJECT SERIALIZER
# =========================================

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"


# =========================================
# CLASS SUBJECT SERIALIZER
# =========================================

class ClassSubjectSerializer(serializers.ModelSerializer):

    class_name = serializers.CharField(
        source="class_obj.name",
        read_only=True
    )

    stream_name = serializers.CharField(
        source="stream.name",
        read_only=True
    )

    subject_name = serializers.CharField(
        source="subject.name",
        read_only=True
    )

    class Meta:
        model = ClassSubject
        fields = "__all__"