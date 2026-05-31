from django.db import models

from apps.communications.communication_categories.models import (
    CommunicationCategory
)


class CommunicationTemplate(
    models.Model
):

    category = models.ForeignKey(
        CommunicationCategory,
        on_delete=models.CASCADE,
        related_name='templates'
    )

    name = models.CharField(
        max_length=200
    )

    subject = models.CharField(
        max_length=255
    )

    content = models.TextField()

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
            'communication_templates'
        )

        ordering = ['name']

    def __str__(self):

        return self.name