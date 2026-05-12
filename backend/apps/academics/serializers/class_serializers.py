from rest_framework import serializers

from apps.academics.models import (
    Class,
    Stream,
    Medium,
    Classroom,
    Section
)


# =========================================
# CLASS SERIALIZER
# =========================================

class ClassSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Class

        fields = "__all__"

        read_only_fields = [
            "school"
        ]


# =========================================
# STREAM SERIALIZER
# =========================================

class StreamSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Stream

        fields = "__all__"

        read_only_fields = [
            "school"
        ]


# =========================================
# MEDIUM SERIALIZER
# =========================================

class MediumSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Medium

        fields = "__all__"

        read_only_fields = [
            "school"
        ]


# =========================================
# CLASSROOM SERIALIZER
# =========================================

class ClassroomSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Classroom

        fields = "__all__"

        read_only_fields = [
            "school"
        ]


# =========================================
# SECTION SERIALIZER
# =========================================

class SectionSerializer(
    serializers.ModelSerializer
):

    class_name = serializers.CharField(
        source="class_obj.name",
        read_only=True
    )

    stream_name = serializers.CharField(
        source="stream.name",
        read_only=True
    )

    medium_name = serializers.CharField(
        source="medium.name",
        read_only=True
    )

    classroom_name = serializers.CharField(
        source="classroom.name",
        read_only=True
    )

    class Meta:

        model = Section

        fields = "__all__"

        read_only_fields = [
            "school"
        ]