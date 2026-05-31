from rest_framework import serializers

from .models import Library


class LibrarySerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(

        source="school.name",

        read_only=True
    )

    room_name = serializers.CharField(

        source="room.room_name",

        read_only=True
    )

    room_number = serializers.CharField(

        source="room.room_number",

        read_only=True
    )

    librarian_name = serializers.CharField(

        source="librarian.full_name",

        read_only=True
    )

    class Meta:

        model = Library

        fields = "__all__"