from django.contrib import admin

from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(
    admin.ModelAdmin
):

    list_display = (
        "question",
        "school",
        "category",
        "order",
        "is_active",
    )

    list_filter = (
        "school",
        "category",
        "is_active",
    )

    search_fields = (
        "question",
        "answer",
    )

    ordering = (
        "order",
    )