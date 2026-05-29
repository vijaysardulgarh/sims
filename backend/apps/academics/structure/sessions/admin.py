# =============================================================================
# academics/sessions/admin.py
# =============================================================================

from django.contrib import admin

from apps.academics.structure.sessions.models import (
    AcademicSession
)


@admin.register(
    AcademicSession
)
class AcademicSessionAdmin(
    admin.ModelAdmin
):

    list_display = (
        "name",
        "school",
        "start_date",
        "end_date",
        "is_current",
    )

    list_filter = (
        "is_current",
        "school",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "-start_date",
    )