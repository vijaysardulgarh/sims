from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(
    admin.ModelAdmin
):

    list_display = (
        "title",
        "school",
        "start_date",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "school",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "venue",
        "organizer",
    )