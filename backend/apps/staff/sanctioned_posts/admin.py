from django.contrib import admin

from apps.staff.sanctioned_posts.models import SanctionedPost


@admin.register(SanctionedPost)
class SanctionedPostAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "school",
        "post_type",
        "sanctioned_posts",
        "regular_working",
        "regular_vacancy",
        "guest_working",
        "hkrnl_working",
        "net_vacancy",
    )

    search_fields = (
        "school__name",
        "post_type__name",
    )

    list_filter = (
        "school",
        "post_type",
    )

    ordering = (
        "school",
        "post_type__name",
    )

    list_per_page = 25