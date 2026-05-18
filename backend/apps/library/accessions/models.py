from django.db import models
from apps.library.books.models import Book
from apps.core.models import SchoolBaseModel

class BookAccession(SchoolBaseModel):

    STATUS_CHOICES = [
        ("available", "Available"),
        ("issued", "Issued"),
        ("lost", "Lost"),
        ("damaged", "Damaged"),
    ]

    accession_number = models.CharField(
        max_length=50,
        unique=True
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="accessions"
    )

    barcode = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    purchase_date = models.DateField(
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    vendor = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    source = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    rack_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    shelf_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    condition = models.CharField(
        max_length=50,
        default="new"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available"
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accession_number