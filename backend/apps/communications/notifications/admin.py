from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(
    admin.ModelAdmin
):

    list_display = (
        "subject",
        "school",
        "notification_type",
        "status",
        "created_at",
    )

    list_filter = (
        "school",
        "notification_type",
        "status",
    )

    search_fields = (
        "subject",
        "message",
    )