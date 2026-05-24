from django.contrib import admin

from apps.academics.structure.sections.models import (
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
    )

    ordering = (
        "class_obj",
        "name",
    )

    list_per_page = 25