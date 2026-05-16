from django.contrib import admin

from apps.staff.models import TeacherAttendance


@admin.register(TeacherAttendance)
class TeacherAttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "teacher",
        "school",
        "date",
        "present",
    )

    search_fields = (
        "teacher__name",
        "school__name",
    )

    list_filter = (
        "school",
        "date",
        "present",
    )

    ordering = (
        "-date",
    )

    list_per_page = 25