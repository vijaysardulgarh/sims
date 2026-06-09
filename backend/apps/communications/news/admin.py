from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(
    admin.ModelAdmin
):

    list_display = (
        "title",
        "school",
        "publish_date",
        "is_published",
        "is_active",
    )

    list_filter = (
        "school",
        "is_published",
        "is_active",
    )

    search_fields = (
        "title",
        "summary",
    )

    ordering = (
        "-publish_date",
    )