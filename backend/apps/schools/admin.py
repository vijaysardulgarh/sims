from django.contrib import admin
from .models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    # ==========================================
    # TABLE DISPLAY
    # ==========================================

    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'website',
        'is_active',
        'created_at',
    )

    list_display_links = (
        'id',
        'name',
    )

    # ==========================================
    # SEARCH
    # ==========================================

    search_fields = (
        'name',
        'email',
        'phone_number',
        'slug',
    )

    # ==========================================
    # FILTERS
    # ==========================================

    list_filter = (
        'is_active',
        'is_deleted',
        'created_at',
    )

    # ==========================================
    # ORDERING
    # ==========================================

    ordering = (
        'name',
    )

    # ==========================================
    # PAGINATION
    # ==========================================

    list_per_page = 25

    # ==========================================
    # READONLY FIELDS
    # ==========================================

    readonly_fields = (
        'slug',
        'created_at',
        'updated_at',
    )

    # ==========================================
    # FIELDSETS
    # ==========================================

    fieldsets = (

        ('Basic Information', {
            'fields': (
                'name',
                'slug',
                'motto',
                'accreditation',
                'established_date',
            )
        }),

        ('Contact Information', {
            'fields': (
                'email',
                'phone_number',
                'website',
                'address',
            )
        }),

        ('Media & Branding', {
            'fields': (
                'logo',
                'social_media_links',
            )
        }),

        ('Status', {
            'fields': (
                'is_active',
                'is_deleted',
            )
        }),

        ('System Information', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )