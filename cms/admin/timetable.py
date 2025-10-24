from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from ..resources.timetable import DayResource,TimetableSlotResource,TimetableResource
from ..models.timetable import Day,TimetableSlot,Timetable

@admin.register(Day)
class DayAdmin(ImportExportModelAdmin):
    resource_class = DayResource
    list_display = ("school", "name", "sequence")
    search_fields = ("name", "school__name")
    list_filter = ("school",)
    ordering = ("school", "sequence")


@admin.register(TimetableSlot)
class TimetableSlotAdmin(ImportExportModelAdmin):
    resource_class = TimetableSlotResource
    list_display = (
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
    list_filter = ("school", "day", "is_break", "is_assembly", "is_special_event")
    ordering = ("school", "day__sequence", "sequence_number")          

@admin.register(Timetable)
class TimetableAdmin(ImportExportModelAdmin):
    resource_class = TimetableResource
    list_display = (
        "school",
        "section",
        "get_class",
        "get_subject",
        "teacher",
        "slot",
        "classroom",
        "substitute_teacher",
    )
    search_fields = (
        "school__name",
        "section__name",
        "class_subject__subject_class__name",
        "class_subject__subject__name",
        "teacher__name",
    )
    list_filter = ['teacher_assignment', 'slot', 'classroom']

    def get_class(self, obj):
        return obj.class_subject.subject_class
    get_class.short_description = "Class"

    def get_subject(self, obj):
        return obj.class_subject.subject
    get_subject.short_description = "Subject"

