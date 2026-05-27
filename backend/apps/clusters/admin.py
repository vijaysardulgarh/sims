from django.contrib import admin

from .models import (
    Cluster
)


# ==========================================
# CLUSTER ADMIN
# ==========================================

@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):

    # ==========================================
    # TABLE DISPLAY
    # ==========================================

    list_display = (
        "id",
        "name",
        "code",
        "email",
        "phone",
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
    )

    # ==========================================
    # FILTERS
    # ==========================================

    list_filter = (
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
            "Basic Information",
            {
                "fields": (
                    "name",
                    "code",
                    "slug",
                    "description",
                )
            }
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "address",
                )
            }
        ),

        (
            "Media",
            {
                "fields": (
                    "logo",
                )
            }
        ),

        (
            "Location",
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