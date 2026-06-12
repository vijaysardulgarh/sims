from django.contrib import admin

from .models import (
    GradeScale
)


@admin.register(
    GradeScale
)
class GradeScaleAdmin(
    admin.ModelAdmin
):

    list_display = [

        "name",

        "code",

        "is_default",

        "is_active",
    ]

    search_fields = [

        "name",

        "code",
    ]

    list_filter = [

        "is_default",

        "is_active",
    ]