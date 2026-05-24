from django.contrib import admin

from apps.academics.curriculum.teacher_subject_assignments.models import (
    TeacherSubjectAssignment
)


@admin.register(TeacherSubjectAssignment)
class TeacherSubjectAssignmentAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "teacher",
        "section",
        "class_subject",
    )

    search_fields = (
        "teacher__name",
        "section__name",
        "class_subject__subject__name",
    )

    list_filter = (
        "teacher__school",
        "section__class_obj",
        "class_subject__subject",
    )

    ordering = (
        "teacher",
        "section",
    )

    autocomplete_fields = (
        "teacher",
        "section",
        "class_subject",
    )

    list_select_related = (
        "teacher",
        "section",
        "class_subject",
    )

    list_per_page = 25