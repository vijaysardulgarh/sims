from django.contrib import admin

from .models import (
    DateSheet
)


@admin.register(
    DateSheet
)
class DateSheetAdmin(
    admin.ModelAdmin
):

    list_display = [

        "exam",

        "class_obj",

        "section",

        "subject",

        "exam_date",

        "start_time",

        "end_time",
    ]

    search_fields = [

        "exam__name",

        "subject__name",
    ]

    list_filter = [

        "exam",

        "class_obj",

        "section",

        "exam_date",
    ]