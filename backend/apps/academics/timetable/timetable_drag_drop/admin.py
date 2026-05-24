from django.contrib import admin

from apps.academics.timetable.timetables.models import (
    Timetable
)


@admin.register(Timetable)
class TimetableAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "teacher_subject_assignment",
        "slot",
    )

    search_fields = (
        "teacher_subject_assignment__teacher__name",

        "teacher_subject_assignment__section__name",

        "teacher_subject_assignment__class_subject__subject__name",
    )

    list_filter = (
        "slot__day",
    )

    ordering = (
        "slot",
    )

    autocomplete_fields = (
        "teacher_subject_assignment",
        "slot",
    )

    list_select_related = (
        "teacher_subject_assignment",
        "slot",
    )

    list_per_page = 25