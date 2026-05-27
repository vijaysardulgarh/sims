# =============================================================================
# associations/admin/association_member_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import AssociationMember


@admin.register(AssociationMember)
class AssociationMemberAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "association",
        "staff",
        "designation",
        "phone_number",
    )

    search_fields = (
        "staff__name",
        "designation",
        "association__name",
    )

    list_filter = (
        "association",
    )

    ordering = (
        "designation",
        "staff",
    )

    list_per_page = 25

    autocomplete_fields = (
        "association",
        "staff",
    )

    list_select_related = (
        "association",
        "staff",
    )