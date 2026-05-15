from django.db import models
from django.utils import timezone


class BookIssue(models.Model):

    STATUS_CHOICES = [
        ("issued", "Issued"),
        ("returned", "Returned"),
        ("late", "Late"),
        ("lost", "Lost"),
    ]

    accession = models.ForeignKey(
        "accessions.BookAccession",
        on_delete=models.CASCADE,
        related_name="issues"
    )

    member = models.ForeignKey(
        "members.LibraryMember",
        on_delete=models.CASCADE,
        related_name="borrowed_books"
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
        default="issued"
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
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.accession.accession_number} - "
            f"{self.member}"
        )