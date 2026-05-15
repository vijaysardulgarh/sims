from rest_framework import serializers

from apps.library.issues.models import (
    BookIssue
)


class BookIssueSerializer(
    serializers.ModelSerializer
):

    accession_number = serializers.CharField(
        source="accession.accession_number",
        read_only=True
    )

    member_name = serializers.CharField(
        source="member.__str__",
        read_only=True
    )

    book_title = serializers.CharField(
        source="accession.book.title",
        read_only=True
    )

    class Meta:

        model = BookIssue

        fields = [

            "id",

            "school",

            "accession",

            "accession_number",

            "book_title",

            "member",

            "member_name",

            "issue_date",

            "due_date",

            "return_date",

            "status",

            "issued_by",

            "returned_by",

            "remarks",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "school",

            "created_at",

            "updated_at",
        ]