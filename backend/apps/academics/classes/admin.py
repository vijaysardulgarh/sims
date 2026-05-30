from django.contrib import admin

from apps.academics.classes.models import (
    Class
)


@admin.register(Class)
class ClassAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "name",
        "school",
        "display_order",
        "is_active",
    )

    search_fields = (
        "name",
        "school__name",
    )

    list_filter = (
        "school",
        "is_active",
    )

    ordering = (
        "display_order",
        "name",
    )

    list_per_page = 25