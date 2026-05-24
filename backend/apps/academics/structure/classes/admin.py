from django.contrib import admin

from apps.academics.structure.classes.models import (
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
        "class_order",
    )

    search_fields = (
        "name",
        "school__name",
    )

    list_filter = (
        "school",
    )

    ordering = (
        "class_order",
        "name",
    )

    list_per_page = 25