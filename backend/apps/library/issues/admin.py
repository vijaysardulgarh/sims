from django.contrib import admin

from apps.library.issues.models import (
    BookIssue
)


@admin.register(BookIssue)
class BookIssueAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "accession",
        "member",
        "issue_date",
        "due_date",
        "return_date",
        "status",
        "school",
    )

    search_fields = (

        "accession__accession_number",

        "member__user__first_name",

        "member__user__last_name",
    )

    list_filter = (
        "school",
        "status",
        "issue_date",
    )

    ordering = (
        "-created_at",
    )

    autocomplete_fields = (
        "accession",
        "member",
        "issued_by",
        "returned_by",
    )

    list_select_related = (
        "school",
        "accession",
        "member",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_per_page = 25