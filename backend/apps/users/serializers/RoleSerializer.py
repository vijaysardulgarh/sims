from rest_framework import serializers

from users.models import (
    Role
)


class RoleSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Role

        fields = "__all__"