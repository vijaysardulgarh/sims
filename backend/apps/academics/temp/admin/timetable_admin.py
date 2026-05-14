from django.contrib import admin

from apps.academics.models import (
    Day,
    TimetableSlot,
    Timetable,
)


# ==========================================
# DAY
# ==========================================

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "school",
        "sequence",
    )

    search_fields = (
        "name",
        "school__name",
    )

    list_filter = (
        "school",
    )

    ordering = (
        "sequence",
    )

    list_per_page = 25


# ==========================================
# TIMETABLE SLOT
# ==========================================

@admin.register(TimetableSlot)
class TimetableSlotAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "school",
        "day",
        "sequence_number",
        "period_number",
        "start_time",
        "end_time",
        "is_break",
        "is_assembly",
        "is_special_event",
    )

    search_fields = (
        "day__name",
        "school__name",
    )

    list_filter = (
        "school",
        "day",
        "is_break",
        "is_assembly",
        "is_special_event",
    )

    ordering = (
        "day",
        "sequence_number",
    )

    list_per_page = 25


# ==========================================
# TIMETABLE
# ==========================================

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "teacher",
        "section",
        "class_subject",
        "slot",
        "classroom",
        "substitute_teacher",
    )

    search_fields = (
        "teacher_subject_assignment__teacher__name",
        "teacher_subject_assignment__section__name",
    )

    list_filter = (
        "school",
        "slot__day",
    )

    ordering = (
        "slot",
    )

    list_per_page = 25

    readonly_fields = (
        "created_at",
        "updated_at",
    )