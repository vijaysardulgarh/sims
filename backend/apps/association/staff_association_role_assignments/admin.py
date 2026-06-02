# =============================================================================
# associations/admin/staff_association_role_assignment_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import StaffAssociationRoleAssignment


@admin.register(StaffAssociationRoleAssignment)
class StaffAssociationRoleAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "staff",
        "role",
        "academic_session",
        "is_active",
    )

    search_fields = (
        "staff__name",
        "role__title",
        "role__association__name",
    )

    list_filter = (
        "academic_session",
        "role__association",
        "is_active",
    )

    ordering = (
        "staff",
    )

    list_per_page = 25

    autocomplete_fields = (
        "staff",
        "role",
        "academic_session",
    )

    list_select_related = (
        "staff",
        "role",
        "academic_session",
    )