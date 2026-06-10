from django.contrib import admin

from .models import (
    ExamType
)


@admin.register(
    ExamType
)
class ExamTypeAdmin(
    admin.ModelAdmin
):

    list_display = [

        "name",

        "code",

        "weightage",

        "is_active",

        "display_order",
    ]

    search_fields = [

        "name",

        "code",
    ]

    list_filter = [

        "is_active",

        "allow_practical",

        "allow_internal_assessment",
    ]