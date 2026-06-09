from django.contrib import admin

from .models import Circular


@admin.register(Circular)
class CircularAdmin(
    admin.ModelAdmin
):

    list_display = (
        "title",
        "school",
        "circular_type",
        "issue_date",
        "is_active",
    )

    list_filter = (
        "school",
        "circular_type",
        "is_active",
    )

    search_fields = (
        "title",
        "reference_number",
    )