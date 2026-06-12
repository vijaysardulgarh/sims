from django.contrib import admin

from .models import (
    BestOfSubject
)


@admin.register(
    BestOfSubject
)
class BestOfSubjectAdmin(
    admin.ModelAdmin
):

    list_display = [

        "name",

        "exam",

        "rule_type",

        "subject_count",

        "is_active",
    ]

    search_fields = [

        "name",

        "exam__name",
    ]

    list_filter = [

        "rule_type",

        "is_active",
    ]