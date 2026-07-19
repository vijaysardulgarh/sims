from django.contrib import admin

from apps.staff.profiles.models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    # ============================================
    # LIST PAGE
    # ============================================

    list_display = (
        "employee_id",
        "name",
        "school",
        "designation",
        "post_type",
        "staff_role",
        "employment_type",
        "status",
        "subject",
        "mobile_number",
        "is_active",
    )

    list_display_links = (
        "employee_id",
        "name",
    )

    search_fields = (
        "employee_id",
        "name",
        "father_name",
        "mother_name",
        "spouse_name",
        "designation",
        "qualification",
        "email",
        "mobile_number",
        "aadhar_number",
        "city",
        "district",
        "state",
        "pin_code",
        "school__name",
        "post_type__name",
        "subject__name",
    )

    list_filter = (
        "school",
        "staff_role",
        "employment_type",
        "designation",
        "status",
        "gender",
        "post_type",
        "subject",
        "city",
        "district",
        "state",
        "is_active",
    )

    ordering = (
        "school",
        "name",
    )

    list_per_page = 25

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # ============================================
    # FORM LAYOUT
    # ============================================

    fieldsets = (

        ("Basic Information", {
            "fields": (
                "school",
                "user",
                "employee_id",
                "name",
                "profile_picture",
                "gender",
            )
        }),

        ("Family Information", {
            "fields": (
                "father_name",
                "mother_name",
                "spouse_name",
            )
        }),

        ("Employment Information", {
            "fields": (
                "post_type",
                "designation",
                "staff_role",
                "employment_type",
                "status",
                "subject",
                "qualification",
                "teaching_experience_years",
            )
        }),

        ("Identity & Contact", {
            "fields": (
                "aadhar_number",
                "email",
                "mobile_number",
            )
        }),

        ("Address Information", {
            "fields": (
                "address",
                "city",
                "district",
                "state",
                "country",
                "pin_code",
            )
        }),

        ("Dates", {
            "fields": (
                "date_of_birth",
                "joining_date",
                "current_joining_date",
                "retirement_date",
            )
        }),

        ("Additional Information", {
            "fields": (
                "category",
                "bio",
                "is_active",
                "is_deleted",
            )
        }),

        ("System Information", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )