# =============================================================================
# associations/admin/association_role_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import AssociationRole


@admin.register(AssociationRole)
class AssociationRoleAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "association",
        "title",
        "is_active",
    )

    search_fields = (
        "title",
        "association__name",
    )

    list_filter = (
        "association__association_type",
        "association__academic_session",
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
    )