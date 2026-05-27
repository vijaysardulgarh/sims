# =============================================================================
# associations/admin/student_association_role_assignment_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import StudentAssociationRoleAssignment


@admin.register(StudentAssociationRoleAssignment)
class StudentAssociationRoleAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "student",
        "role",
        "academic_session",
        "is_active",
    )

    search_fields = (
        "student__full_name_aadhar",
        "student__srn",
        "role__title",
        "role__association__name",
    )

    list_filter = (
        "academic_session",
        "role__association",
        "is_active",
    )

    ordering = (
        "student",
    )

    list_per_page = 25

    autocomplete_fields = (
        "student",
        "role",
        "academic_session",
    )

    list_select_related = (
        "student",
        "role",
        "academic_session",
    )