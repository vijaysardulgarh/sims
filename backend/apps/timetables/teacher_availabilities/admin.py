from django.contrib import admin

from .models import TeacherAvailability


@admin.register(TeacherAvailability)
class TeacherAvailabilityAdmin(admin.ModelAdmin):

    # ============================================
    # LIST
    # ============================================

    list_display = (
        "teacher",
        "employee_id",
        "day",
        "period",
        "is_available",
        "reason",
        "school",
        "academic_session",
        "is_active",
    )

    # ============================================
    # SEARCH
    # ============================================

    search_fields = (
        "teacher__employee_id",
        "teacher__name",
        "reason",
    )

    # ============================================
    # FILTERS
    # ============================================

    list_filter = (
        "school",
        "academic_session",
        "day",
        "period",
        "is_available",
        "is_active",
    )

    # ============================================
    # ORDERING
    # ============================================

    ordering = (
        "teacher__employee_id",
        "day",
        "period",
    )

    # ============================================
    # READONLY
    # ============================================

    readonly_fields = (
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
        "deleted_at",
        "deleted_by",
    )

    # ============================================
    # PERFORMANCE
    # ============================================

    list_select_related = (
        "teacher",
        "period",
        "school",
        "academic_session",
    )

    # ============================================
    # HELPERS
    # ============================================

    @admin.display(
        description="Employee ID",
        ordering="teacher__employee_id",
    )
    def employee_id(self, obj):
        return obj.teacher.employee_id