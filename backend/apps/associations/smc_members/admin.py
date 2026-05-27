# =============================================================================
# associations/admin/smc_member_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import SMCMember


@admin.register(SMCMember)
class SMCMemberAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "position",
        "academic_session",
        "school",
        "contact_number",
        "show_on_website",
    )

    search_fields = (
        "name",
        "position",
        "school__name",
    )

    list_filter = (
        "position",
        "academic_session",
        "show_on_website",
        "school",
    )

    ordering = (
        "priority",
        "name",
    )

    list_per_page = 25

    autocomplete_fields = (
        "academic_session",
    )

    list_select_related = (
        "school",
        "academic_session",
    )