from django.contrib import admin

from .models import (
    AdmitCard
)


@admin.register(
    AdmitCard
)
class AdmitCardAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "exam",

        "roll_number",

        "issue_date",

        "is_generated",
    ]

    search_fields = [

        "student__full_name",

        "roll_number",
    ]

    list_filter = [

        "exam",

        "is_generated",
    ]