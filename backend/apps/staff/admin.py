from django.contrib import admin
from .models import (
    PostType,
    Staff,
    ClassIncharge,
    SanctionedPost,
    TeacherSubjectAssignment,
    TeacherAttendance,
)


# ==========================================
# POST TYPE
# ==========================================

@admin.register(PostType)
class PostTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )

    search_fields = (
        'name',
    )

    ordering = (
        'name',
    )


# ==========================================
# STAFF
# ==========================================

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    list_display = (
        'employee_id',
        'name',
        'school',
        'post_type',
        'staff_role',
        'employment_type',
        'subject',
        'mobile_number',
        'is_active',
    )

    list_display_links = (
        'employee_id',
        'name',
    )

    search_fields = (
        'employee_id',
        'name',
        'father_name',
        'email',
        'mobile_number',
        'aadhar_number',
        'school__name',
    )

    list_filter = (
        'school',
        'staff_role',
        'employment_type',
        'gender',
        'post_type',
        'is_active',
    )

    ordering = (
        'school',
        'name',
    )

    list_per_page = 25

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    fieldsets = (

        ('Basic Information', {
            'fields': (
                'school',
                'employee_id',
                'name',
                'profile_picture',
                'gender',
            )
        }),

        ('Family Information', {
            'fields': (
                'father_name',
                'mother_name',
                'spouse_name',
            )
        }),

        ('Employment Information', {
            'fields': (
                'post_type',
                'staff_role',
                'employment_type',
                'subject',
                'qualification',
                'priority',
                'max_periods_per_week',
            )
        }),

        ('Identity & Contact', {
            'fields': (
                'aadhar_number',
                'email',
                'mobile_number',
            )
        }),

        ('Dates', {
            'fields': (
                'date_of_birth',
                'joining_date',
                'current_joining_date',
                'retirement_date',
            )
        }),

        ('Additional Information', {
            'fields': (
                'category',
                'bio',
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


# ==========================================
# CLASS INCHARGE
# ==========================================

@admin.register(ClassIncharge)
class ClassInchargeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'section',
        'staff',
        'effective_from',
        'effective_to',
        'active',
    )

    search_fields = (
        'staff__name',
        'section__name',
    )

    list_filter = (
        'active',
        'effective_from',
    )

    ordering = (
        '-effective_from',
    )

    list_per_page = 25


# ==========================================
# SANCTIONED POSTS
# ==========================================

@admin.register(SanctionedPost)
class SanctionedPostAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'school',
        'post_type',
        'designation',
        'subject',
        'total_posts',
    )

    search_fields = (
        'designation',
        'school__name',
    )

    list_filter = (
        'school',
        'post_type',
    )

    ordering = (
        'school',
        'designation',
    )

    list_per_page = 25


# ==========================================
# TEACHER SUBJECT ASSIGNMENT
# ==========================================

@admin.register(TeacherSubjectAssignment)
class TeacherSubjectAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'teacher',
        'section',
        'class_subject',
    )

    search_fields = (
        'teacher__name',
        'section__name',
    )

    list_filter = (
        'section',
    )

    ordering = (
        'teacher',
    )

    list_per_page = 25


# ==========================================
# TEACHER ATTENDANCE
# ==========================================

@admin.register(TeacherAttendance)
class TeacherAttendanceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'teacher',
        'school',
        'date',
        'present',
    )

    search_fields = (
        'teacher__name',
        'school__name',
    )

    list_filter = (
        'school',
        'date',
        'present',
    )

    ordering = (
        '-date',
    )

    list_per_page = 25