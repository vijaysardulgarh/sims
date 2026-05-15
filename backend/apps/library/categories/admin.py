from django.contrib import admin

from apps.library.categories.models import (
    BookCategory
)


@admin.register(BookCategory)
class BookCategoryAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "name",
        "code",
        "is_active",
        "school",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "school",
        "is_active",
    )

    ordering = (
        "name",
    )

    list_select_related = (
        "school",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_per_page = 25