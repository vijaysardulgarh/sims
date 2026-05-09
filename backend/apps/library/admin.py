from django.contrib import admin
from .models import (
    Book,
    BookIssue,
)


# ==========================================
# BOOK ADMIN
# ==========================================

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    # Table columns
    list_display = (
        'id',
        'title',
        'author',
        'school',
        'category',
        'total_copies',
        'available_copies',
        'is_active',
    )

    # Clickable fields
    list_display_links = (
        'id',
        'title',
    )

    # Search
    search_fields = (
        'title',
        'author',
        'isbn',
        'school__name',
    )

    # Filters
    list_filter = (
        'category',
        'is_active',
        'school',
    )

    # Ordering
    ordering = (
        'title',
    )

    # Pagination
    list_per_page = 25

    # Readonly fields
    readonly_fields = (
        'created_at',
        'updated_at',
    )

    # Form sections
    fieldsets = (

        ('Basic Information', {
            'fields': (
                'school',
                'title',
                'author',
                'isbn',
                'publication_date',
            )
        }),

        ('Inventory Information', {
            'fields': (
                'category',
                'total_copies',
                'available_copies',
                'is_active',
            )
        }),

        ('System Information', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )


# ==========================================
# BOOK ISSUE ADMIN
# ==========================================

@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):

    # Table columns
    list_display = (
        'id',
        'student',
        'book',
        'issue_date',
        'due_date',
        'return_date',
        'is_returned',
        'fine_amount',
    )

    # Clickable fields
    list_display_links = (
        'id',
        'student',
    )

    # Search
    search_fields = (
        'student__full_name_aadhar',
        'student__srn',
        'book__title',
        'book__author',
    )

    # Filters
    list_filter = (
        'is_returned',
        'issue_date',
        'due_date',
        'book__school',
    )

    # Ordering
    ordering = (
        '-created_at',
    )

    # Pagination
    list_per_page = 25

    # Readonly fields
    readonly_fields = (
        'fine_amount',
        'created_at',
    )

    # Form sections
    fieldsets = (

        ('Issue Information', {
            'fields': (
                'student',
                'book',
            )
        }),

        ('Dates', {
            'fields': (
                'issue_date',
                'due_date',
                'return_date',
            )
        }),

        ('Return Status', {
            'fields': (
                'is_returned',
                'fine_amount',
            )
        }),

        ('System Information', {
            'fields': (
                'created_at',
            )
        }),
    )