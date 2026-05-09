from django.contrib import admin
from .models import (
    FeeStructure,
    StudentFee,
    FeePayment,
)


# ==========================================
# FEE STRUCTURE ADMIN
# ==========================================

@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):

    # Table columns
    list_display = (
        'id',
        'school',
        'class_obj',
        'stream',
        'session',
        'total_fee',
        'is_active',
    )

    # Clickable fields
    list_display_links = (
        'id',
        'class_obj',
    )

    # Search
    search_fields = (
        'school__name',
        'class_obj__name',
        'session',
    )

    # Filters
    list_filter = (
        'school',
        'session',
        'is_active',
    )

    # Ordering
    ordering = (
        '-session',
        'class_obj',
    )

    # Pagination
    list_per_page = 25

    # Readonly fields
    readonly_fields = (
        'total_fee',
        'created_at',
        'updated_at',
    )

    # Form sections
    fieldsets = (

        ('Academic Information', {
            'fields': (
                'school',
                'class_obj',
                'stream',
                'session',
            )
        }),

        ('Fee Components', {
            'fields': (
                'admission_fee',
                'rcf',
                'cwf',
                'ccwf',
                'other_fee',
                'total_fee',
            )
        }),

        ('Status', {
            'fields': (
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
# STUDENT FEE ADMIN
# ==========================================

@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):

    # Table columns
    list_display = (
        'id',
        'student',
        'session',
        'total_amount',
        'paid_amount',
        'due_amount',
        'is_closed',
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
        'session',
    )

    # Filters
    list_filter = (
        'session',
        'is_closed',
    )

    # Ordering
    ordering = (
        '-created_at',
    )

    # Pagination
    list_per_page = 25

    # Readonly fields
    readonly_fields = (
        'due_amount',
        'is_closed',
        'created_at',
    )

    # Form sections
    fieldsets = (

        ('Student Fee Information', {
            'fields': (
                'student',
                'fee_structure',
                'session',
            )
        }),

        ('Amounts', {
            'fields': (
                'total_amount',
                'paid_amount',
                'due_amount',
            )
        }),

        ('Status', {
            'fields': (
                'is_closed',
            )
        }),

        ('System Information', {
            'fields': (
                'created_at',
            )
        }),
    )


# ==========================================
# FEE PAYMENT ADMIN
# ==========================================

@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):

    # Table columns
    list_display = (
        'id',
        'student_fee',
        'amount',
        'payment_mode',
        'receipt_number',
        'payment_date',
    )

    # Clickable fields
    list_display_links = (
        'id',
        'receipt_number',
    )

    # Search
    search_fields = (
        'receipt_number',
        'transaction_id',
        'student_fee__student__full_name_aadhar',
        'student_fee__student__srn',
    )

    # Filters
    list_filter = (
        'payment_mode',
        'payment_date',
    )

    # Ordering
    ordering = (
        '-created_at',
    )

    # Pagination
    list_per_page = 25

    # Readonly fields
    readonly_fields = (
        'receipt_number',
        'created_at',
    )

    # Form sections
    fieldsets = (

        ('Payment Information', {
            'fields': (
                'student_fee',
                'amount',
                'payment_mode',
                'transaction_id',
            )
        }),

        ('Receipt Information', {
            'fields': (
                'receipt_number',
                'payment_date',
            )
        }),

        ('System Information', {
            'fields': (
                'created_at',
            )
        }),
    )