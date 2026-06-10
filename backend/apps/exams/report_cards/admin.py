from django.contrib import admin

from .models import (
    ReportCard
)


@admin.register(
    ReportCard
)
class ReportCardAdmin(
    admin.ModelAdmin
):

    list_display = [

        "report_card_number",

        "student",

        "exam",

        "issue_date",

        "is_published",
    ]

    search_fields = [

        "report_card_number",

        "student__full_name",
    ]

    list_filter = [

        "exam",

        "is_published",
    ]