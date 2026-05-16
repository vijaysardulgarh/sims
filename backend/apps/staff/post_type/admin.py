from django.contrib import admin

from apps.staff.models import PostType


@admin.register(PostType)
class PostTypeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )