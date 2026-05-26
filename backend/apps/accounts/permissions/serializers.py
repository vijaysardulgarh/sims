from rest_framework import serializers

from apps.accounts.permissions.models import (
    Permission
)


# ==========================================
# PERMISSION SERIALIZER
# ==========================================

class PermissionSerializer(
    serializers.ModelSerializer
):

    # ======================================
    # OPTIONAL DESCRIPTION
    # ======================================

    description = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )

    # ======================================
    # READONLY MODULE NAME
    # ======================================

    module_name = serializers.CharField(
        source="module.name",
        read_only=True
    )

    # ======================================
    # ACTION DISPLAY
    # ======================================

    action_display = serializers.CharField(
        source="get_action_display",
        read_only=True
    )

    # ======================================
    # MODULE SLUG
    # ======================================

    module_slug = serializers.CharField(
        source="module.slug",
        read_only=True
    )

    class Meta:

        model = Permission

        fields = [

            "id",

            "module",

            "module_name",

            "module_slug",

            "action",

            "action_display",

            "name",

            "code",

            "description",

            "is_active",

            "is_system_permission",

            "display_order",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "id",

            "name",

            "code",

            "created_at",

            "updated_at",
        ]

    # ======================================
    # VALIDATE ACTION
    # ======================================

    def validate_action(
        self,
        value
    ):

        return value.lower()

    # ======================================
    # VALIDATE
    # ======================================

    def validate(
        self,
        attrs
    ):

        module = attrs.get(
            "module"
        )

        action = attrs.get(
            "action"
        )

        # ==================================
        # PREVENT DUPLICATE
        # ==================================

        queryset = Permission.objects.filter(

            module=module,

            action=action,
        )

        if self.instance:

            queryset = queryset.exclude(
                id=self.instance.id
            )

        if queryset.exists():

            raise serializers.ValidationError({

                "action":

                    "Permission already exists "
                    "for this module."
            })

        return attrs