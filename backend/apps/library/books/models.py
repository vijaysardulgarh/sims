from django.db import models

from django.db.models import (
    Q
)

from django.core.exceptions import (
    ValidationError
)

from apps.core.common.base.models import SchoolBaseModel

class Book(SchoolBaseModel):

    STATUS_CHOICES = [

        ("available", "Available"),

        ("issued", "Issued"),

        ("lost", "Lost"),

        ("damaged", "Damaged"),
    ]


    title = models.CharField(
        max_length=255,
        db_index=True
    )

    isbn = models.CharField(
        max_length=20,
        unique=True,
        db_index=True
    )

    author = models.CharField(
        max_length=255,
        db_index=True
    )

    publisher = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=100,
        db_index=True
    )

    language = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    total_copies = models.PositiveIntegerField(
        default=1
    )

    available_copies = models.PositiveIntegerField(
        default=1
    )

    rack_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available",
        db_index=True
    )

    description = models.TextField(
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
            "title"
        ]

        indexes = [

            models.Index(
                fields=["title"]
            ),

            models.Index(
                fields=["author"]
            ),

            models.Index(
                fields=["category"]
            ),

            models.Index(
                fields=["status"]
            ),

            models.Index(
                fields=["school"]
            ),
        ]

        constraints = [

            models.CheckConstraint(
                condition=Q(total_copies__gte=0),
                name="book_total_copies_positive"
            ),

            models.CheckConstraint(
                condition=Q(available_copies__gte=0),
                name="book_available_copies_positive"
            ),

            models.CheckConstraint(
                condition=Q(price__gte=0),
                name="book_price_positive"
            ),
        ]

    def clean(self):

        if self.total_copies < 0:

            raise ValidationError({
                "total_copies":
                    (
                        "Total copies cannot "
                        "be negative"
                    )
            })

        if self.available_copies < 0:

            raise ValidationError({
                "available_copies":
                    (
                        "Available copies "
                        "cannot be negative"
                    )
            })

        if (
            self.available_copies >
            self.total_copies
        ):

            raise ValidationError({
                "available_copies":
                    (
                        "Available copies "
                        "cannot exceed total copies"
                    )
            })

        if self.price < 0:

            raise ValidationError({
                "price":
                    (
                        "Price cannot "
                        "be negative"
                    )
            })

    def save(self, *args, **kwargs):

        if self.title:

            self.title = (
                self.title.strip().title()
            )

        if self.author:

            self.author = (
                self.author.strip().title()
            )

        if self.publisher:

            self.publisher = (
                self.publisher.strip().title()
            )

        if self.category:

            self.category = (
                self.category.strip().title()
            )

        if self.language:

            self.language = (
                self.language.strip().title()
            )

        if self.isbn:

            self.isbn = (
                self.isbn.strip().upper()
            )

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.title