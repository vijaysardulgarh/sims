from django.contrib import admin

from apps.academics.subjects import (
    Subject
)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

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