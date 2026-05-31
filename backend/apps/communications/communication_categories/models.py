from django.db import models


class CommunicationCategory(models.Model):

    name = models.CharField(
        max_length=100
    )

    code = models.CharField(
        max_length=50,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        db_table = (
            'communication_categories'
        )

        ordering = ['name']

    def __str__(self):

        return self.name