# =============================================================================
# associations/admin/association_role_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import (
    AssociationRole
)


@admin.register(AssociationRole)
class AssociationRoleAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "association",
        "academic_session",
        "title",
        "is_active",
    )

    search_fields = (
        "title",
        "responsibilities",
        "association__name",
    )

    list_filter = (
        "school",
        "academic_session",
        "association__association_type",
        "is_active",
    )

    ordering = (
        "association",
        "title",
    )

    list_per_page = 25

    autocomplete_fields = (
        "association",
    )

    list_select_related = (
        "association",
        "academic_session",
        "school",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )