from django.contrib import admin

from .models import (
    ExamTimetableEntry,
)


@admin.register(
    ExamTimetableEntry
)
class ExamTimetableEntryAdmin(
    admin.ModelAdmin
):

    list_display = (
        "subject",
        "school_class",
        "section",
        "exam_date",
        "start_time",
        "end_time",
        "maximum_marks",
        "invigilator",
        "is_active",
    )

    search_fields = (
        "subject__name",
    )

    list_filter = (
        "school",
        "academic_session",
        "exam_date",
        "is_active",
    )