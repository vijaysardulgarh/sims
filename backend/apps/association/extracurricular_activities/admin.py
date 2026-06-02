# =============================================================================
# associations/admin/extracurricular_activity_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import ExtracurricularActivity


@admin.register(ExtracurricularActivity)
class ExtracurricularActivityAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "academic_session",
        "school",
        "category",
        "status",
        "coordinator",
        "start_date",
        "end_date",
        "priority",
    )

    list_display_links = (
        "id",
        "name",
    )

    search_fields = (
        "name",
        "school__name",
        "coordinator__name",
    )

    list_filter = (
        "category",
        "status",
        "academic_session",
        "school",
    )

    ordering = (
        "priority",
        "name",
    )

    list_per_page = 25

    filter_horizontal = (
        "participants",
    )

    autocomplete_fields = (
        "academic_session",
        "coordinator",
    )

    list_select_related = (
        "school",
        "academic_session",
        "coordinator",
    )

    fieldsets = (

        ("Activity Information", {
            "fields": (
                "school",
                "academic_session",
                "name",
                "category",
                "status",
                "priority",
                "description",
            )
        }),

        ("Schedule & Location", {
            "fields": (
                "start_date",
                "end_date",
                "location",
            )
        }),

        ("Coordination", {
            "fields": (
                "coordinator",
                "participants",
            )
        }),

        ("Additional Information", {
            "fields": (
                "cost",
                "capacity",
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