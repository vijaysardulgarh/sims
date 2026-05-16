from django.contrib import admin

from apps.library.issues.models import (
    BookIssue
)


@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "accession",
        "issue_date",
        "due_date",
        "return_date",
        "status",
        "school",
        "issued_by",
        "returned_by",
    )

    search_fields = (
        "accession__accession_number",
        "issued_by__first_name",
        "issued_by__last_name",
        "returned_by__first_name",
        "returned_by__last_name",
    )

    list_filter = (
        "school",
        "status",
        "issue_date",
        "due_date",
    )

    ordering = (
        "-created_at",
    )

    autocomplete_fields = (
        "accession",
        "issued_by",
        "returned_by",
    )

    list_select_related = (
        "school",
        "accession",
        "issued_by",
        "returned_by",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_per_page = 25