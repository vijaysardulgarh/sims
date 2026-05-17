from rest_framework import serializers

from .models import TransportAssignment


class TransportAssignmentSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = TransportAssignment
        fields = "__all__"