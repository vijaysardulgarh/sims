from rest_framework import serializers

from .models import (
    ResourceAllocation,
)


class ResourceAllocationSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = (
            ResourceAllocation
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