from django.contrib import admin

from apps.academics.models import (
    Subject,
    ClassSubject,
)


# ==========================================
# SUBJECT
# ==========================================

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


# ==========================================
# CLASS SUBJECT
# ==========================================

@admin.register(ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):

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