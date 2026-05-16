from rest_framework import serializers

from apps.staff.post_type.models import (
    PostType
)


class PostTypeSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = PostType

        fields = [
            "id",
            "name",
            "description",
        ]