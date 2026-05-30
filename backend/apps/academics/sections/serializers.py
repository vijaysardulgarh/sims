from rest_framework import serializers

from apps.academics.sections.models import (
    Section
)


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

        fields = [

            "id",

            "school",

            "class_obj",
            "class_name",

            "name",

            "classroom",
            "classroom_name",

            "medium",
            "medium_name",

            "stream",
            "stream_name",

            "sub_stream",

            "is_active",

            "created_at",
            "updated_at",
        ]

        read_only_fields = [

            "school",

            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):

        class_obj = attrs.get(
            "class_obj",
            getattr(
                self.instance,
                "class_obj",
                None
            )
        )

        stream = attrs.get(
            "stream",
            getattr(
                self.instance,
                "stream",
                None
            )
        )

        sub_stream = attrs.get(
            "sub_stream",
            getattr(
                self.instance,
                "sub_stream",
                None
            )
        )

        if sub_stream and not stream:

            raise serializers.ValidationError(
                {
                    "sub_stream":
                    "Sub-stream requires a stream."
                }
            )

        return attrs