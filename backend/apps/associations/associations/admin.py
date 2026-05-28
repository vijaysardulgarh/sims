# =============================================================================
# associations/admin/association_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import Association


@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):

    # ============================================
    # LIST PAGE
    # ============================================

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

    ordering = (
        "-priority",
        "name",
    )

    list_per_page = 25

    date_hierarchy = "created_at"

    # ============================================
    # SEARCH
    # ============================================

    search_fields = (
        "name",
        "slug",
        "school__name",
        "chairperson__name",
    )

    # ============================================
    # FILTERS
    # ============================================

    list_filter = (
        "association_type",
        "status",
        "show_on_website",
        "is_active",
        "is_deleted",
        "academic_session",
        "school",
    )

    # ============================================
    # PERFORMANCE
    # ============================================

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

    # ============================================
    # READONLY
    # ============================================

    readonly_fields = (
        "slug",
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
    )

    # ============================================
    # FIELDSETS
    # ============================================

    fieldsets = (

        (
            "Association Information",
            {
                "fields": (
                    "school",
                    "academic_session",
                    "name",
                    "association_type",
                    "slug",
                    "chairperson",
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
            "Website & Status",
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
            "System Information",
            {
                "classes": ("collapse",),

                "fields": (
                    "created_at",
                    "updated_at",
                    "created_by",
                    "updated_by",
                )
            }
        ),
    )

    # ============================================
    # QUERYSET OPTIMIZATION
    # ============================================

    def get_queryset(self, request):

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

    # ============================================
    # AUTO AUDIT FIELDS
    # ============================================

    def save_model(
        self,
        request,
        obj,
        form,
        change
    ):

        if not obj.pk:

            obj.created_by = request.user

        obj.updated_by = request.user

        super().save_model(
            request,
            obj,
            form,
            change
        )