# =============================================================================
# associations/admin/association_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import (
    Association
)


@admin.register(
    Association
)
class AssociationAdmin(
    admin.ModelAdmin
):

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
        "is_active",
    )

    list_display_links = (
        "id",
        "name",
    )

    list_editable = (
        "status",
        "show_on_website",
        "priority",
        "is_active",
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
        "is_active",
        "is_deleted",
        "academic_session",
        "school",
    )

    ordering = (
        "-priority",
        "name",
    )

    list_per_page = 25

    date_hierarchy = "created_at"

    list_select_related = (
        "school",
        "academic_session",
        "chairperson",
        "created_by",
        "updated_by",
    )

    autocomplete_fields = (
        "chairperson",
    )

    filter_horizontal = (
        "documents",
    )

    readonly_fields = (
        "slug",
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
    )

    fieldsets = (

        (
            "Association Information",
            {
                "fields": (
                    "school",
                    "academic_session",
                    "name",
                    "association_type",
                    "chairperson",
                    "slug",
                    "priority",
                )
            }
        ),

        (
            "Description & Tasks",
            {
                "fields": (
                    "description",
                    "tasks",
                )
            }
        ),

        (
            "Documents",
            {
                "fields": (
                    "documents",
                )
            }
        ),

        (
            "Status",
            {
                "fields": (
                    "status",
                    "show_on_website",
                    "is_active",
                    "is_deleted",
                )
            }
        ),

        (
            "Audit Information",
            {
                "classes": (
                    "collapse",
                ),

                "fields": (
                    "created_at",
                    "updated_at",
                    "created_by",
                    "updated_by",
                )
            }
        ),
    )

    def get_queryset(
        self,
        request
    ):

        return (

            super()

            .get_queryset(request)

            .select_related(
                "school",
                "academic_session",
                "chairperson",
                "created_by",
                "updated_by",
            )

            .prefetch_related(
                "documents"
            )
        )

    def save_model(
        self,
        request,
        obj,
        form,
        change
    ):

        if not obj.pk:

            obj.created_by = (
                request.user
            )

        obj.updated_by = (
            request.user
        )

        super().save_model(
            request,
            obj,
            form,
            change
        )