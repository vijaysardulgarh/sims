from django.contrib import admin

from apps.staff.models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    list_display = (
        "employee_id",
        "name",
        "school",
        "post_type",
        "staff_role",
        "employment_type",
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
        "email",
        "mobile_number",
        "aadhar_number",
        "school__name",
    )

    list_filter = (
        "school",
        "staff_role",
        "employment_type",
        "gender",
        "post_type",
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

    fieldsets = (

        ("Basic Information", {
            "fields": (
                "school",
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
                "staff_role",
                "employment_type",
                "subject",
                "qualification",
                "priority",
                "max_periods_per_week",
            )
        }),

        ("Identity & Contact", {
            "fields": (
                "aadhar_number",
                "email",
                "mobile_number",
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
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )