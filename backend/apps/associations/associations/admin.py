# =============================================================================
# associations/admin/association_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import Association


@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "association_type",
        "academic_session",
        "school",
        "chairperson",
        "status",
        "show_on_website",
        "priority",
    )

    list_display_links = (
        "id",
        "name",
    )

    search_fields = (
        "name",
        "slug",
        "school__name",
        "chairperson__name",
    )

    list_filter = (
        "association_type",
        "status",
        "show_on_website",
        "academic_session",
        "school",
    )

    ordering = (
        "priority",
        "name",
    )

    list_per_page = 25

    readonly_fields = (
        "slug",
        "created_at",
        "updated_at",
    )

    filter_horizontal = (
        "documents",
    )

    autocomplete_fields = (
        "chairperson",
    )

    list_select_related = (
        "school",
        "academic_session",
        "chairperson",
    )

    fieldsets = (

        ("Association Information", {
            "fields": (
                "school",
                "academic_session",
                "name",
                "association_type",
                "slug",
                "chairperson",
                "priority",
            )
        }),

        ("Description & Tasks", {
            "fields": (
                "description",
                "tasks",
            )
        }),

        ("Documents", {
            "fields": (
                "documents",
            )
        }),

        ("Website & Status", {
            "fields": (
                "status",
                "show_on_website",
            )
        }),

        ("System Information", {
            "fields": (
                "is_active",
                "created_at",
                "updated_at",
                "created_by",
                "updated_by",
            )
        }),
    )