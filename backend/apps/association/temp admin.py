from django.contrib import admin
from .models import (
    Association,
    AssociationRole,
    StaffAssociationRoleAssignment,
    StudentAssociationRoleAssignment,
    AssociationMember,
    AssociationMeeting,
    SMCMember,
    ExtracurricularActivity,
)


# ==========================================
# ASSOCIATION
# ==========================================

@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'association_type',
        'school',
        'chairperson',
        'show_on_website',
        'is_active',
    )

    list_display_links = (
        'id',
        'name',
    )

    search_fields = (
        'name',
        'school__name',
        'chairperson__name',
        'slug',
    )

    list_filter = (
        'association_type',
        'show_on_website',
        'is_active',
        'school',
    )

    ordering = (
        'name',
    )

    list_per_page = 25

    readonly_fields = (
        'slug',
        'created_at',
        'updated_at',
    )

    filter_horizontal = (
        'documents',
    )

    fieldsets = (

        ('Association Information', {
            'fields': (
                'school',
                'name',
                'association_type',
                'slug',
                'chairperson',
            )
        }),

        ('Description & Tasks', {
            'fields': (
                'description',
                'tasks',
            )
        }),

        ('Documents', {
            'fields': (
                'documents',
            )
        }),

        ('Website & Status', {
            'fields': (
                'show_on_website',
                'is_active',
            )
        }),

        ('System Information', {
            'fields': (
                'created_at',
                'updated_at',
                'created_by',
                'updated_by',
            )
        }),
    )


# ==========================================
# ASSOCIATION ROLE
# ==========================================

@admin.register(AssociationRole)
class AssociationRoleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'association',
        'title',
        'is_active',
    )

    search_fields = (
        'title',
        'association__name',
    )

    list_filter = (
        'association',
        'is_active',
    )

    ordering = (
        'association',
        'title',
    )

    list_per_page = 25


# ==========================================
# STAFF ROLE ASSIGNMENT
# ==========================================

@admin.register(StaffAssociationRoleAssignment)
class StaffAssociationRoleAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'staff',
        'role',
        'is_active',
    )

    search_fields = (
        'staff__name',
        'role__title',
        'role__association__name',
    )

    list_filter = (
        'role__association',
        'is_active',
    )

    ordering = (
        'staff',
    )

    list_per_page = 25


# ==========================================
# STUDENT ROLE ASSIGNMENT
# ==========================================

@admin.register(StudentAssociationRoleAssignment)
class StudentAssociationRoleAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student',
        'role',
        'is_active',
    )

    search_fields = (
        'student__full_name_aadhar',
        'student__srn',
        'role__title',
    )

    list_filter = (
        'role__association',
        'is_active',
    )

    ordering = (
        'student',
    )

    list_per_page = 25


# ==========================================
# ASSOCIATION MEMBER
# ==========================================

@admin.register(AssociationMember)
class AssociationMemberAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'association',
        'staff',
        'designation',
        'phone_number',
    )

    search_fields = (
        'staff__name',
        'designation',
        'association__name',
    )

    list_filter = (
        'association',
    )

    ordering = (
        'designation',
        'staff',
    )

    list_per_page = 25


# ==========================================
# ASSOCIATION MEETING
# ==========================================

@admin.register(AssociationMeeting)
class AssociationMeetingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'association',
        'meeting_date',
        'location',
    )

    search_fields = (
        'association__name',
        'location',
    )

    list_filter = (
        'association',
        'meeting_date',
    )

    ordering = (
        '-meeting_date',
    )

    list_per_page = 25


# ==========================================
# SMC MEMBER
# ==========================================

@admin.register(SMCMember)
class SMCMemberAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'position',
        'school',
        'contact_number',
        'show_on_website',
    )

    search_fields = (
        'name',
        'position',
        'school__name',
    )

    list_filter = (
        'position',
        'show_on_website',
        'school',
    )

    ordering = (
        'priority',
        'name',
    )

    list_per_page = 25


# ==========================================
# EXTRACURRICULAR ACTIVITY
# ==========================================

@admin.register(ExtracurricularActivity)
class ExtracurricularActivityAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
        'category',
        'coordinator',
        'start_date',
        'end_date',
        'active',
    )

    list_display_links = (
        'id',
        'name',
    )

    search_fields = (
        'name',
        'school__name',
        'coordinator__name',
    )

    list_filter = (
        'category',
        'active',
        'school',
    )

    ordering = (
        'name',
    )

    list_per_page = 25

    filter_horizontal = (
        'participants',
    )

    fieldsets = (

        ('Activity Information', {
            'fields': (
                'school',
                'name',
                'category',
                'description',
            )
        }),

        ('Schedule & Location', {
            'fields': (
                'start_date',
                'end_date',
                'location',
            )
        }),

        ('Coordination', {
            'fields': (
                'coordinator',
                'participants',
            )
        }),

        ('Additional Information', {
            'fields': (
                'cost',
                'capacity',
                'active',
            )
        }),

        ('System Information', {
            'fields': (
                'is_active',
                'created_at',
                'updated_at',
                'created_by',
                'updated_by',
            )
        }),
    )