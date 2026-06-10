from django.contrib import admin

from .models import (
    GradeCalculation
)


@admin.register(
    GradeCalculation
)
class GradeCalculationAdmin(
    admin.ModelAdmin
):

    list_display = [

        "grade",

        "minimum_percentage",

        "maximum_percentage",

        "grade_point",
    ]

    search_fields = [

        "grade",
    ]

    ordering = [

        "-minimum_percentage",
    ]