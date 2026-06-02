# =============================================================================
# associations/admin/member_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.members.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "group",
        "staff",
        "designation",
        "phone_number",
    )

    search_fields = (
        "staff__name",
        "designation",
        "group__name",
    )

    list_filter = (
        "group",
    )

    ordering = (
        "designation",
        "staff",
    )

    list_per_page = 25

    autocomplete_fields = (
        "group",
        "staff",
    )

    list_select_related = (
        "group",
        "staff",
    )