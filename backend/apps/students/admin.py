from django.contrib import admin
from .models import (
    Student,
    StudentAchievement,
    ExamDetail,
)


# ==========================================
# STUDENT
# ==========================================

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    # Table display
    list_display = (
        'srn',
        'full_name_aadhar',
        'student_class',
        'section',
        'roll_number',
        'gender',
        'category',
        'father_mobile',
        'school',
    )

    # Clickable fields
    list_display_links = (
        'srn',
        'full_name_aadhar',
    )

    # Search
    search_fields = (
        'srn',
        'full_name_aadhar',
        'father_full_name_aadhar',
        'mother_full_name_aadhar',
        'aadhaar_number',
        'admission_number',
        'father_mobile',
        'mother_mobile',
        'school',
    )

    # Filters
    list_filter = (
        'student_class',
        'section',
        'gender',
        'category',
        'religion',
        'school',
    )

    # Ordering
    ordering = (
        'student_class',
        'section',
        'roll_number',
    )

    # Pagination
    list_per_page = 25

    # Read only fields
    readonly_fields = (
        'subjects',
    )

    # Field grouping
    fieldsets = (

        ('School Information', {
            'fields': (
                'srn',
                'school_code',
                'school',
                'admission_date',
                'admission_number',
            )
        }),

        ('Academic Information', {
            'fields': (
                'student_class',
                'stream',
                'section',
                'roll_number',
                'subjects_opted',
                'subjects',
            )
        }),

        ('Student Personal Information', {
            'fields': (
                'full_name_aadhar',
                'date_of_birth',
                'gender',
                'aadhaar_number',
                'religion',
                'category',
                'caste',
                'domicile_of_haryana',
            )
        }),

        ('Parents Information', {
            'fields': (
                'father_full_name_aadhar',
                'father_aadhaar_number',
                'father_mobile',

                'mother_full_name_aadhar',
                'mother_aadhaar_number',
                'mother_mobile',
            )
        }),

        ('Financial Information', {
            'fields': (
                'family_annual_income',
                'account_number',
                'bank_name',
                'ifsc',
                'family_id',
                'below_poverty_line_certificate_number',
                'bpl_certificate_issuing_authority',
            )
        }),

        ('Address Information', {
            'fields': (
                'state',
                'district',
                'block',
                'sub_district',
                'city_village_town',
                'address',
                'postal_code',
            )
        }),

        ('Medical / Disability Information', {
            'fields': (
                'disability',
                'disorder',
            )
        }),
    )


# ==========================================
# STUDENT ACHIEVEMENT
# ==========================================

@admin.register(StudentAchievement)
class StudentAchievementAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student_name',
        'achievement_type',
        'event_name',
        'rank',
        'date',
    )

    search_fields = (
        'student_name',
        'event_name',
        'reward_title',
    )

    list_filter = (
        'achievement_type',
        'date',
    )

    ordering = (
        '-date',
    )

    list_per_page = 25


# ==========================================
# EXAM DETAIL
# ==========================================

@admin.register(ExamDetail)
class ExamDetailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'achievement',
        'obtained_marks',
        'total_marks',
        'percentage',
    )

    search_fields = (
        'achievement__student_name',
    )

    ordering = (
        '-id',
    )

    list_per_page = 25