from django.contrib import admin

from .models import Module


@admin.register(Module)
class ModuleAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "name",
        "slug",
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": (
            "name",
        )
    }