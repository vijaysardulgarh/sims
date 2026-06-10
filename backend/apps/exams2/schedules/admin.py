from django.contrib import admin

from apps.exams.models import ExamSchedule


@admin.register(ExamSchedule)
class ExamScheduleAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "exam",
        "class_name",
        "section",
        "subject",
        "exam_date",
        "start_time",
        "end_time",
        "room",
        "invigilator",
        "max_marks",
        "passing_marks",
    )

    list_filter = (
        "exam",
        "class_name",
        "section",
        "exam_date",
    )

    search_fields = (
        "subject",
        "room",
        "invigilator",
        "exam__name",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )