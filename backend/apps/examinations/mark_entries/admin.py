from django.contrib import admin

from .models import (
    MarkEntry
)


@admin.register(
    MarkEntry
)
class MarkEntryAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "subject",

        "exam",

        "theory_marks",

        "practical_marks",

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