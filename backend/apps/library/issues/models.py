from django.db import models

from django.db.models import (
    Q
)

from django.core.exceptions import (
    ValidationError
)

from django.utils import timezone


class BookIssue(models.Model):

    STATUS_CHOICES = [

        ("issued", "Issued"),

        ("returned", "Returned"),

        ("late", "Late"),

        ("lost", "Lost"),
    ]

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="book_issues",
        db_index=True
    )

    accession = models.ForeignKey(
        "accessions.BookAccession",
        on_delete=models.CASCADE,
        related_name="issues",
        db_index=True
    )

    member = models.ForeignKey(
        "members.LibraryMember",
        on_delete=models.CASCADE,
        related_name="borrowed_books",
        db_index=True
    )

    issue_date = models.DateField(
        default=timezone.now
    )

    due_date = models.DateField()

    return_date = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="issued",
        db_index=True
    )

    issued_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="issued_books"
    )

    returned_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="returned_books"
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "-created_at"
        ]

        indexes = [

            models.Index(
                fields=["status"]
            ),

            models.Index(
                fields=["issue_date"]
            ),

            models.Index(
                fields=["due_date"]
            ),

            models.Index(
                fields=["school"]
            ),
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "accession"
                ],

                condition=Q(
                    status="issued"
                ),

                name=(
                    "unique_active_issue_"
                    "per_accession"
                )
            )
        ]

    def clean(self):

        if (
            self.due_date <
            self.issue_date
        ):

            raise ValidationError({
                "due_date":
                    (
                        "Due date cannot be "
                        "before issue date"
                    )
            })

        if (
            self.return_date and
            self.return_date < self.issue_date
        ):

            raise ValidationError({
                "return_date":
                    (
                        "Return date cannot "
                        "be before issue date"
                    )
            })

    def save(self, *args, **kwargs):

        is_new = self.pk is None

        self.full_clean()

        super().save(*args, **kwargs)

        if is_new:

            self.accession.status = (
                "issued"
            )

            self.accession.save()

        if self.status == "returned":

            self.accession.status = (
                "available"
            )

            self.accession.save()

    def __str__(self):

        return (

            f"{self.accession.accession_number}"

            f" - "

            f"{self.member}"
        )