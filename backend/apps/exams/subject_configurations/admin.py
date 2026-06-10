from django.contrib import admin

from .models import (
    SubjectConfiguration
)


@admin.register(
    SubjectConfiguration
)
class SubjectConfigurationAdmin(
    admin.ModelAdmin
):

    list_display = [

        "exam",

        "subject",

        "maximum_marks",

        "passing_marks",
    ]

    search_fields = [

        "exam__name",

        "subject__name",
    ]

    list_filter = [

        "exam",

        "is_practical_enabled",

        "is_internal_enabled",
    ]