from django.contrib import admin
from .models import (
    Class,
    Stream,
    Medium,
    Classroom,
    Section,
    Subject,
    ClassSubject,
    Day,
    TimetableSlot,
    Timetable,
)


# ==========================================
# CLASS
# ==========================================

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
        'class_order',
    )

    search_fields = (
        'name',
        'school__name',
    )

    list_filter = (
        'school',
    )

    ordering = (
        'class_order',
        'name',
    )

    list_per_page = 25


# ==========================================
# STREAM
# ==========================================

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
    )

    search_fields = (
        'name',
        'school__name',
    )

    list_filter = (
        'school',
    )

    ordering = (
        'name',
    )

    list_per_page = 25


# ==========================================
# MEDIUM
# ==========================================

@admin.register(Medium)
class MediumAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
    )

    search_fields = (
        'name',
        'school__name',
    )

    list_filter = (
        'school',
    )

    ordering = (
        'name',
    )

    list_per_page = 25


# ==========================================
# CLASSROOM
# ==========================================

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
        'capacity',
        'floor',
    )

    search_fields = (
        'name',
        'school__name',
    )

    list_filter = (
        'school',
    )

    ordering = (
        'name',
    )

    list_per_page = 25


# ==========================================
# SECTION
# ==========================================

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'class_obj',
        'name',
        'school',
        'stream',
        'sub_stream',
        'medium',
        'classroom',
    )

    search_fields = (
        'name',
        'class_obj__name',
        'school__name',
    )

    list_filter = (
        'school',
        'stream',
        'medium',
        'sub_stream',
    )

    ordering = (
        'class_obj',
        'name',
    )

    list_per_page = 25


# ==========================================
# SUBJECT
# ==========================================

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
    )

    search_fields = (
        'name',
        'school__name',
    )

    list_filter = (
        'school',
    )

    ordering = (
        'name',
    )

    list_per_page = 25


# ==========================================
# CLASS SUBJECT
# ==========================================

@admin.register(ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'class_obj',
        'subject',
        'stream',
        'sub_stream',
        'periods_per_week',
        'is_optional',
        'has_lab',
    )

    search_fields = (
        'subject__name',
        'class_obj__name',
    )

    list_filter = (
        'stream',
        'sub_stream',
        'is_optional',
        'has_lab',
    )

    ordering = (
        'class_obj',
        'subject',
    )

    list_per_page = 25

    readonly_fields = (
        'periods_per_week',
    )


# ==========================================
# DAY
# ==========================================

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
        'sequence',
    )

    search_fields = (
        'name',
        'school__name',
    )

    list_filter = (
        'school',
    )

    ordering = (
        'sequence',
    )

    list_per_page = 25


# ==========================================
# TIMETABLE SLOT
# ==========================================

@admin.register(TimetableSlot)
class TimetableSlotAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'school',
        'day',
        'sequence_number',
        'period_number',
        'start_time',
        'end_time',
        'is_break',
        'is_assembly',
        'is_special_event',
    )

    search_fields = (
        'day__name',
        'school__name',
    )

    list_filter = (
        'school',
        'day',
        'is_break',
        'is_assembly',
        'is_special_event',
    )

    ordering = (
        'day',
        'sequence_number',
    )

    list_per_page = 25


# ==========================================
# TIMETABLE
# ==========================================

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'teacher',
        'section',
        'class_subject',
        'slot',
        'classroom',
        'substitute_teacher',
    )

    search_fields = (
        'teacher_subject_assignment__teacher__name',
        'teacher_subject_assignment__section__name',
    )

    list_filter = (
        'school',
        'slot__day',
    )

    ordering = (
        'slot',
    )

    list_per_page = 25

    readonly_fields = (
        'created_at',
        'updated_at',
    )