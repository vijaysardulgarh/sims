from django.contrib import admin

from apps.exams.models import Exam


@admin.register(Exam)
class ExamAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "name",
        "exam_type",
        "exam_mode",
        "grading_system",
        "academic_year",
        "start_date",
        "end_date",
        "status",
        "school",
    )

    list_filter = (
        "exam_mode",
        "grading_system",
        "status",
        "academic_year",
        "school",
    )

    search_fields = (
        "name",
        "exam_type",
        "academic_year",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )