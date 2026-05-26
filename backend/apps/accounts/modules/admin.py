from django.contrib import admin

from .models import Module


@admin.register(Module)
class ModuleAdmin(
    admin.ModelAdmin
):

    # =====================================
    # LIST PAGE
    # =====================================

    list_display = (
        "id",
        "name",
        "parent",
        "path",
        "icon",
        "order",
        "is_menu",
        "is_active",
    )

    # =====================================
    # FILTERS
    # =====================================

    list_filter = (
        "is_active",
        "is_menu",
        "parent",
    )

    # =====================================
    # SEARCH
    # =====================================

    search_fields = (
        "name",
        "slug",
        "path",
    )

    # =====================================
    # AUTO SLUG
    # =====================================

    prepopulated_fields = {
        "slug": (
            "name",
        )
    }

    # =====================================
    # DEFAULT ORDERING
    # =====================================

    ordering = (
        "order",
        "name",
    )

    # =====================================
    # ADMIN FORM LAYOUT
    # =====================================

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "parent",
                    "name",
                    "slug",
                )
            }
        ),

        (
            "Frontend Settings",
            {
                "fields": (
                    "path",
                    "icon",
                    "order",
                    "is_menu",
                )
            }
        ),

        (
            "Status",
            {
                "fields": (
                    "is_active",
                    "is_deleted",
                )
            }
        ),
    )