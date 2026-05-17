from django.contrib import admin

from .models import TransportAssignment


@admin.register(TransportAssignment)
class TransportAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        "student_name",
        "route",
        "stop",
        "monthly_fee",
        "active",
    )

    search_fields = (
        "student_name",
    )