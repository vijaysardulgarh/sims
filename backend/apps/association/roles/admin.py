# =============================================================================
# associations/roles/admin/role_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.roles.models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "group",
        "title",
        "is_active",
    )

    search_fields = (
        "title",
        "group__name",
    )

    list_filter = (
        "group__group_type",
        "group__academic_session",
        "is_active",
    )

    ordering = (
        "group",
        "title",
    )

    list_per_page = 25

    autocomplete_fields = (
        "group",
    )

    list_select_related = (
        "group",
    )