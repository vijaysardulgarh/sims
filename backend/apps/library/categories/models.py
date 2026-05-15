# library/categories/models.py

from django.db import models


class BookCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Book Category"
        verbose_name_plural = "Book Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name