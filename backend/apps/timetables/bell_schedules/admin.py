from django.contrib import admin

from .models import BellSchedule


@admin.register(
    BellSchedule
)
class BellScheduleAdmin(
    admin.ModelAdmin
):

    list_display = (
        "name",
        "code",
        "school",
        "academic_session",
        "is_default",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "school",
        "is_default",
        "is_active",
    )