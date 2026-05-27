from django.contrib import admin

from .models import (
    School
)

#=======================================
# SCHOOL ADMIN
# ==========================================

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    # ==========================================
    # TABLE DISPLAY
    # ==========================================

    list_display = (
        "id",
        "name",
        "code",
        "email",
        "phone",
        "school_type",
        "board",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "id",
        "name",
    )

    # ==========================================
    # SEARCH
    # ==========================================

    search_fields = (
        "name",
        "code",
        "email",
        "slug",
        "city",
    )

    # ==========================================
    # FILTERS
    # ==========================================

    list_filter = (
        "school_type",
        "board",
        "is_active",
        "created_at",
    )

    # ==========================================
    # ORDERING
    # ==========================================

    ordering = (
        "name",
    )

    # ==========================================
    # PAGINATION
    # ==========================================

    list_per_page = 25

    # ==========================================
    # READONLY FIELDS
    # ==========================================

    readonly_fields = (
        "slug",
        "created_at",
        "updated_at",
    )

    # ==========================================
    # FIELDSETS
    # ==========================================

    fieldsets = (

        (
            "Cluster Information",
            {
                "fields": (
                    "cluster",
                )
            }
        ),

        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "code",
                    "slug",
                    "subdomain",
                    "motto",
                    "logo",
                )
            }
        ),

        (
            "Academic Information",
            {
                "fields": (
                    "school_type",
                    "board",
                    "language",
                    "academic_year_start_month",
                    "affiliation_number",
                    "accreditation",
                    "established_date",
                )
            }
        ),

        (
            "Management",
            {
                "fields": (
                    "principal_name",
                )
            }
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "alternate_phone",
                    "website",
                )
            }
        ),

        (
            "Address",
            {
                "fields": (
                    "address",
                    "city",
                    "state",
                    "country",
                    "pincode",
                )
            }
        ),

        (
            "Social Media",
            {
                "fields": (
                    "social_media_links",
                )
            }
        ),

        (
            "GPS & Geofence",
            {
                "fields": (
                    "latitude",
                    "longitude",
                    "geo_radius_meters",
                )
            }
        ),

        (
            "Regional Settings",
            {
                "fields": (
                    "timezone",
                    "currency",
                )
            }
        ),

        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),
    )
