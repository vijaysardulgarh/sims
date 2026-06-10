from django.contrib import admin

from .models import (
    PracticalExam
)


@admin.register(
    PracticalExam
)
class PracticalExamAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "subject",

        "exam",

        "practical_date",

        "total_marks",

        "is_absent",
    ]

    search_fields = [

        "student__full_name",

        "subject__name",
    ]

    list_filter = [

        "exam",

        "subject",

        "is_absent",
    ]