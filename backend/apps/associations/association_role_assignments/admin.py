# =============================================================================
# association_role_assignments/admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import (
    AssociationRoleAssignment
)


@admin.register(
    AssociationRoleAssignment
)
class AssociationRoleAssignmentAdmin(
    admin.ModelAdmin
):

    # ============================================
    # LIST DISPLAY
    # ============================================

    list_display = (

        "id",

        "get_association",

        "get_member",

        "role",

        "academic_session",

        "is_active",
    )

    # ============================================
    # SEARCH
    # ============================================

    search_fields = (

        "role__title",

        "member__association__name",

        "member__staff__name",

        "member__student__full_name_aadhar",

        "member__external_name",
    )

    # ============================================
    # FILTERS
    # ============================================

    list_filter = (

        "academic_session",

        "role__association",

        "role",

        "is_active",
    )

    # ============================================
    # AUTOCOMPLETE
    # ============================================

    autocomplete_fields = (

        "member",

        "role",

        "academic_session",
    )

    # ============================================
    # PERFORMANCE
    # ============================================

    list_select_related = (

        "member",

        "member__association",

        "member__staff",

        "member__student",

        "role",

        "academic_session",
    )

    # ============================================
    # ORDERING
    # ============================================

    ordering = (

        "role__title",
    )

    list_per_page = 25

    # ============================================
    # CUSTOM COLUMNS
    # ============================================

    @admin.display(
        description="Association"
    )
    def get_association(
        self,
        obj
    ):

        return (
            obj.member.association.name
        )

    @admin.display(
        description="Member"
    )
    def get_member(
        self,
        obj
    ):

        return (
            obj.member.member_name
        )