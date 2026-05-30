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

        visited = self.context.get(
            "visited",
            set(),
        )

        if obj.id in visited:
            return []

        visited.add(obj.id)

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
            context={
                "visited": visited,
            },
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

    def validate_parent(
        self,
        value
    ):

        if (
            self.instance
            and value
            and value.id == self.instance.id
        ):
            raise serializers.ValidationError(
                "A module cannot be its own parent."
            )

        current = value

        while current:

            if (
                self.instance
                and current.id == self.instance.id
            ):
                raise serializers.ValidationError(
                    "Circular parent relationship detected."
                )

            current = current.parent

        return value