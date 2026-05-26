from rest_framework import serializers

from .models import Module


class RecursiveModuleSerializer(
    serializers.ModelSerializer
):

    children = serializers.SerializerMethodField()

    class Meta:

        model = Module

        fields = [
            "id",
            "name",
            "slug",
            "path",
            "icon",
            "order",
            "is_menu",
            "is_active",
            "children",
        ]

    def get_children(
        self,
        obj
    ):

        children = obj.children.filter(
            is_deleted=False,
            is_active=True,
        ).order_by(
            "order",
            "name",
        )

        return RecursiveModuleSerializer(
            children,
            many=True,
        ).data


class ModuleSerializer(
    serializers.ModelSerializer
):

    parent_name = serializers.CharField(
        source="parent.name",
        read_only=True,
    )

    children = RecursiveModuleSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Module

        fields = [
            "id",

            "parent",
            "parent_name",

            "name",
            "slug",

            "path",
            "icon",

            "order",

            "is_menu",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",

            "children",
        ]