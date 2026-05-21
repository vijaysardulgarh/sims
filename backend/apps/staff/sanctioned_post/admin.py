from django.contrib import admin

from apps.staff.sanctioned_post.models import SanctionedPost


@admin.register(SanctionedPost)
class SanctionedPostAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "school",
        "post_type",
        "designation",
        "subject",
        "total_posts",
    )

    search_fields = (
        "designation",
        "school__name",
    )

    list_filter = (
        "school",
        "post_type",
    )

    ordering = (
        "school",
        "designation",
    )

    list_per_page = 25