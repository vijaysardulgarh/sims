from django.contrib import admin

from .models import (
    GraceMark
)


@admin.register(
    GraceMark
)
class GraceMarkAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "exam",

        "subject",

        "original_marks",

        "grace_marks",

        "final_marks",

        "approved",
    ]

    search_fields = [

        "student__full_name",

        "subject__name",
    ]

    list_filter = [

        "approved",

        "exam",
    ]