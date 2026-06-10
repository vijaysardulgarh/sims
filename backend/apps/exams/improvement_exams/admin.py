from django.contrib import admin

from .models import (
    ImprovementExam
)


@admin.register(
    ImprovementExam
)
class ImprovementExamAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "subject",

        "original_exam",

        "original_marks",

        "improvement_marks",

        "final_marks",

        "status",
    ]

    search_fields = [

        "student__full_name",

        "subject__name",
    ]

    list_filter = [

        "status",

        "subject",

        "original_exam",
    ]