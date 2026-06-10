from django.contrib import admin

from .models import (
    Revaluation
)


@admin.register(
    Revaluation
)
class RevaluationAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "subject",

        "exam",

        "original_marks",

        "revised_marks",

        "marks_difference",

        "status",
    ]

    search_fields = [

        "student__full_name",

        "subject__name",
    ]

    list_filter = [

        "status",

        "exam",

        "subject",
    ]