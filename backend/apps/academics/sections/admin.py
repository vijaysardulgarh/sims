from django.contrib import admin

from apps.academics.sections.models import (
    Section
)


@admin.register(Section)
class SectionAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "class_obj",
        "name",
        "school",
        "stream",
        "sub_stream",
        "medium",
        "classroom",
        "is_active",
    )

    search_fields = (
        "name",
        "class_obj__name",
        "school__name",
    )

    list_filter = (
        "school",
        "stream",
        "medium",
        "sub_stream",
        "is_active",
    )

    ordering = (
        "class_obj__display_order",
        "class_obj__name",
        "name",
    )

    list_select_related = (
        "school",
        "class_obj",
        "stream",
        "medium",
        "classroom",
    )

    list_per_page = 25