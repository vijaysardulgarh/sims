from rest_framework import serializers

from apps.users.models.access_control_model import (
    AccessControl
)


# ==========================================
# ACCESS CONTROL SERIALIZER
# ==========================================

class AccessControlSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = AccessControl

        fields = "__all__"