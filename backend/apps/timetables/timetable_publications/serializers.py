from rest_framework import serializers
from .models import *

class DefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = list(globals().values())[0]
        fields = '__all__'
from rest_framework import serializers

from .models import (
    TimetablePublication,
)


class TimetablePublicationSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = (
            TimetablePublication
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