from django.contrib import admin

from .models import (
    Exam
)


@admin.register(
    Exam
)
class ExamAdmin(
    admin.ModelAdmin
):

    list_display = [

        "name",

        "exam_type",

        "start_date",

        "end_date",

        "is_marks_locked",

        "is_result_published",
    ]

    search_fields = [

        "name",

        "exam_type__name",
    ]

    list_filter = [

        "exam_type",

        "is_marks_locked",

        "is_result_published",
    ]