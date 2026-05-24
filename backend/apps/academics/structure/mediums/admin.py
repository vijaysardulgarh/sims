from django.contrib import admin

from apps.academics.structure.mediums.models import (
    Medium
)


@admin.register(Medium)
class MediumAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "name",
        "school",
    )

    search_fields = (
        "name",
        "school__name",
    )

    list_filter = (
        "school",
    )

    ordering = (
        "name",
    )

    list_per_page = 25