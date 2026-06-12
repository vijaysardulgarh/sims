from django.contrib import admin

from .models import (
    InternalAssessment
)


@admin.register(
    InternalAssessment
)
class InternalAssessmentAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "subject",

        "exam",

        "assignment_marks",

        "project_marks",

        "notebook_marks",

        "attendance_marks",

        "total_marks",
    ]

    search_fields = [

        "student__full_name",

        "subject__name",
    ]

    list_filter = [

        "exam",

        "subject",
    ]