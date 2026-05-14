from django.contrib import admin

from apps.academics.classrooms import (
    Classroom
)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "school",
        "capacity",
        "floor",
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