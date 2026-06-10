from rest_framework import serializers

from .models import (
    TimetableConflict,
)


class TimetableConflictSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = (
            TimetableConflict
        )

        fields = "__all__"

        read_only_fields = (
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "deleted_at",
            "deleted_by",
        )