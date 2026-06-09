from django.contrib import admin

from .models import CommunicationCategory


@admin.register(CommunicationCategory)
class CommunicationCategoryAdmin(
    admin.ModelAdmin
):

    list_display = (
        "name",
        "code",
        "school",
        "is_active",
    )

    list_filter = (
        "school",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )