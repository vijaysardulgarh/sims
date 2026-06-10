from django.contrib import admin

from apps.exams.models import ExamType


@admin.register(ExamType)
class ExamTypeAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "name",
        "code",
        "category",
        "default_max_marks",
        "default_passing_marks",
        "is_internal",
        "is_practical",
        "is_online",
        "has_viva",
        "has_assignment",
        "is_active",
        "school",
    )

    list_filter = (
        "category",
        "is_internal",
        "is_practical",
        "is_online",
        "has_viva",
        "has_assignment",
        "is_active",
        "school",
    )

    search_fields = (
        "name",
        "code",
        "description",
    )

    ordering = (
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    prepopulated_fields = {
        "code": ("name",)
    }