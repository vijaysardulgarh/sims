from django.contrib import admin

from .models import (
    ResultPublication
)


@admin.register(
    ResultPublication
)
class ResultPublicationAdmin(
    admin.ModelAdmin
):

    list_display = [

        "exam",

        "publication_date",

        "is_published",

        "notification_sent",
    ]

    search_fields = [

        "exam__name",
    ]

    list_filter = [

        "is_published",

        "notification_sent",
    ]