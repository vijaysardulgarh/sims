from django.db import models

from django.core.exceptions import (
    ValidationError
)

from apps.schools.models import School
from apps.core.models import SchoolBaseModel

class BookCategory(SchoolBaseModel):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="book_categories",
        db_index=True
    )

    name = models.CharField(
        max_length=100,
        db_index=True
    )

    code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        db_index=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True,
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name = (
            "Book Category"
        )

        verbose_name_plural = (
            "Book Categories"
        )

        ordering = [
            "name"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "name"
                ],
                name=(
                    "unique_book_category_"
                    "per_school"
                )
            ),

            models.UniqueConstraint(
                fields=[
                    "school",
                    "code"
                ],
                name=(
                    "unique_book_category_code_"
                    "per_school"
                )
            ),
        ]

    def clean(self):

        if self.name:

            self.name = (
                self.name.strip().title()
            )

        if self.code:

            self.code = (
                self.code.strip().upper()
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name