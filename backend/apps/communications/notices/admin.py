from django.contrib import admin

from .models import Notice


@admin.register(Notice)
class NoticeAdmin(
    admin.ModelAdmin
):

    list_display = (
        "title",
        "school",
        "notice_type",
        "publish_date",
        "is_published",
    )

    list_filter = (
        "school",
        "notice_type",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
    )