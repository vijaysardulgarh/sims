from django.contrib import admin

from apps.timetables.class_subjects.models import (
    ClassSubject
)


@admin.register(ClassSubject)
class ClassSubjectAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "class_obj",
        "subject",
        "stream",
        "sub_stream",
        "periods_per_week",
        "is_optional",
        "has_lab",
    )

    search_fields = (
        "subject__name",
        "class_obj__name",
    )

    list_filter = (
        "stream",
        "sub_stream",
        "is_optional",
        "has_lab",
    )

    ordering = (
        "class_obj",
        "subject",
    )

    list_per_page = 25

    readonly_fields = (
        "periods_per_week",
    )