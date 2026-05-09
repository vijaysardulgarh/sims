from django.contrib import admin
from .models import (
    Student,
    StudentAchievement,
    ExamDetail,
)


# ==========================================
# STUDENT ADMIN
# ==========================================

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    # --------------------------------------
    # TABLE DISPLAY
    # --------------------------------------

    list_display = (
        'srn',
        'full_name_aadhar',
        'school',
        'student_class',
        'section',
        'roll_number',
        'gender',
        'category',
        'father_mobile',
    )

    list_display_links = (
        'srn',
        'full_name_aadhar',
    )

    # --------------------------------------
    # SEARCH
    # --------------------------------------

    search_fields = (
        'srn',
        'full_name_aadhar',
        'father_full_name_aadhar',
        'mother_full_name_aadhar',
        'aadhaar_number',
        'admission_number',
        'father_mobile',
        'mother_mobile',

        # ForeignKey searches
        'school__name',
        'student_class__name',
        'stream__name',
        'section__name',
    )

    # --------------------------------------
    # FILTERS
    # --------------------------------------

    list_filter = (
        'school',
        'student_class',
        'stream',
        'section',
        'gender',
        'category',
        'religion',
    )

    # --------------------------------------
    # ORDERING
    # --------------------------------------

    ordering = (
        'school',
        'student_class',
        'section',
        'roll_number',
    )

    # --------------------------------------
    # AUTOCOMPLETE FIELDS
    # --------------------------------------

    autocomplete_fields = (
        'school',
        'student_class',
        'stream',
        'section',
    )

    # --------------------------------------
    # PAGINATION
    # --------------------------------------

    list_per_page = 25

    # --------------------------------------
    # READONLY
    # --------------------------------------

    readonly_fields = (
        'subjects',
    )

    # --------------------------------------
    # FIELDSETS
    # --------------------------------------

    fieldsets = (

        ('School Information', {
            'fields': (
                'school',
                'school_code',
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
                'srn',
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
# STUDENT ACHIEVEMENT ADMIN
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
# EXAM DETAIL ADMIN
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