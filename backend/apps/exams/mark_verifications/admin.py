from django.contrib import admin

from .models import (
    MarkVerification
)


@admin.register(
    MarkVerification
)
class MarkVerificationAdmin(
    admin.ModelAdmin
):

    list_display = [

        "mark_entry",

        "status",

        "verified_by",

        "verified_at",
    ]

    search_fields = [

        "mark_entry__student__full_name",

        "mark_entry__subject__name",
    ]

    list_filter = [

        "status",
    ]