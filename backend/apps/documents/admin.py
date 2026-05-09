from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    # ==========================================
    # TABLE DISPLAY
    # ==========================================

    list_display = (
        'id',
        'title',
        'school',
        'file_type',
        'formatted_file_size',
        'uploaded_at',
    )

    list_display_links = (
        'id',
        'title',
    )

    # ==========================================
    # SEARCH
    # ==========================================

    search_fields = (
        'title',
        'school__name',
        'file_type',
    )

    # ==========================================
    # FILTERS
    # ==========================================

    list_filter = (
        'file_type',
        'uploaded_at',
        'school',
    )

    # ==========================================
    # ORDERING
    # ==========================================

    ordering = (
        '-uploaded_at',
    )

    # ==========================================
    # PAGINATION
    # ==========================================

    list_per_page = 25

    # ==========================================
    # READONLY FIELDS
    # ==========================================

    readonly_fields = (
        'file_size',
        'file_type',
        'uploaded_at',
        'file_preview',
    )

    # ==========================================
    # FIELDSETS
    # ==========================================

    fieldsets = (

        ('Document Information', {
            'fields': (
                'school',
                'title',
                'file',
                'file_preview',
            )
        }),

        ('File Metadata', {
            'fields': (
                'file_type',
                'file_size',
                'uploaded_at',
            )
        }),
    )

    # ==========================================
    # CUSTOM METHODS
    # ==========================================

    def formatted_file_size(self, obj):

        if not obj.file_size:
            return "0 Bytes"

        size = obj.file_size

        for unit in ['Bytes', 'KB', 'MB', 'GB']:

            if size < 1024:
                return f"{size:.2f} {unit}"

            size /= 1024

        return f"{size:.2f} TB"

    formatted_file_size.short_description = "File Size"

    def file_preview(self, obj):

        if obj.file:
            return f"Uploaded File: {obj.file.name}"

        return "No File"

    file_preview.short_description = "File Preview"