from rest_framework import serializers


class UserPermissionSerializer(
    serializers.Serializer
):

    id = serializers.IntegerField()

    full_name = serializers.CharField()

    email = serializers.EmailField()

    school = serializers.CharField()

    roles = serializers.ListField()

    permissions = serializers.ListField()