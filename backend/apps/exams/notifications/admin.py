from django.contrib import admin

from apps.exams.models import ExamNotification


@admin.register(ExamNotification)
class ExamNotificationAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "title",
        "exam",
        "notification_type",
        "is_published",
        "published_at",
        "school",
        "created_at",
    )

    list_filter = (
        "notification_type",
        "is_published",
        "school",
    )

    search_fields = (
        "title",
        "message",
        "exam__name",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )