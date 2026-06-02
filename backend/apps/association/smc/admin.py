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
        "contact_number",
        "nomination_date",
        "tenure_end_date",
        "show_on_website",
        "academic_session",
        "school",
    )

    search_fields = (
        "name",
        "position",
        "contact_number",
        "email",
        "remarks",
        "school__name",
    )

    list_filter = (
        "position",
        "gender",
        "category",
        "show_on_website",
        "academic_session",
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

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "position",
                    "gender",
                    "category",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "contact_number",
                    "email",
                    "address",
                )
            },
        ),
        (
            "Tenure Information",
            {
                "fields": (
                    "nomination_date",
                    "tenure_end_date",
                )
            },
        ),
        (
            "Media & Display",
            {
                "fields": (
                    "photo",
                    "priority",
                    "show_on_website",
                )
            },
        ),
        (
            "Additional Information",
            {
                "fields": (
                    "remarks",
                )
            },
        ),
    )