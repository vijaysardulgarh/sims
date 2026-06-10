from rest_framework import serializers

from .models import (
    WorkingDay,
)


class WorkingDaySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = (
            WorkingDay
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