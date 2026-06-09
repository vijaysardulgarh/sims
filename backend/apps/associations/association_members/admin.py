# =============================================================================
# associations/admin/association_member_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.models import (
    AssociationMember
)


@admin.register(AssociationMember)
class AssociationMemberAdmin(
    admin.ModelAdmin
):

    list_display = (

        "id",

        "association",

        "member_type",

        "member_name",

        "email",

        "phone_number",

        "academic_session",

        "is_active",
    )

    search_fields = (

        "association__name",

        "staff__name",

        "student__full_name",

        "external_name",

        "email",

        "phone_number",
    )

    list_filter = (

        "member_type",

        "association",

        "academic_session",

        "is_active",
    )

    ordering = (

        "association",

        "member_type",
    )

    list_per_page = 25

    autocomplete_fields = (

        "association",

        "academic_session",

        "staff",

        "student",
    )

    list_select_related = (

        "association",

        "academic_session",

        "staff",

        "student",
    )

    readonly_fields = (

        "created_at",

        "updated_at",
    )

    fieldsets = (

        (
            "Association Information",
            {
                "fields": (

                    "academic_session",

                    "association",

                    "member_type",
                )
            },
        ),

        (
            "Internal Member",
            {
                "fields": (

                    "staff",

                    "student",
                )
            },
        ),

        (
            "External Member",
            {
                "fields": (

                    "external_name",

                    "external_email",

                    "external_phone_number",

                    "external_designation",

                    "image",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (

                    "is_active",

                    "is_deleted",
                )
            },
        ),

        (
            "Audit",
            {
                "classes": (
                    "collapse",
                ),

                "fields": (

                    "created_at",

                    "updated_at",
                )
            },
        ),
    )

    def member_name(
        self,
        obj
    ):

        if obj.staff:
            return obj.staff.name

        if obj.student:
            return getattr(
                obj.student,
                "full_name",
                str(obj.student)
            )

        return obj.external_name

    member_name.short_description = (
        "Member"
    )