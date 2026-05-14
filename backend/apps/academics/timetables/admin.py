from django.contrib import admin

from apps.academics.timetables import (
    Timetable
)


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "teacher",
        "section",
        "class_subject",
        "slot",
        "classroom",
        "substitute_teacher",
    )

    search_fields = (
        "teacher_subject_assignment"
        "__teacher__name",

        "teacher_subject_assignment"
        "__section__name",
    )

    list_filter = (
        "school",
        "slot__day",
    )

    ordering = (
        "slot",
    )

    list_per_page = 25

    readonly_fields = (
        "created_at",
        "updated_at",
    )