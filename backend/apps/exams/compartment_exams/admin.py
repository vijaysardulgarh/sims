from django.contrib import admin

from .models import (
    CompartmentExam
)


@admin.register(
    CompartmentExam
)
class CompartmentExamAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "subject",

        "original_exam",

        "exam_date",

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