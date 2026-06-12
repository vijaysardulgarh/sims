from django.contrib import admin

from .models import (
    ResultGeneration
)


@admin.register(
    ResultGeneration
)
class ResultGenerationAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "exam",

        "percentage",

        "overall_grade",

        "class_rank",

        "result_status",
    ]

    search_fields = [

        "student__full_name",

        "exam__name",
    ]

    list_filter = [

        "result_status",

        "is_published",
    ]