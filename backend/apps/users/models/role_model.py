from django.db import models

from apps.core.models import (
    AuditBaseModel
)


# ==========================================
# ROLE MODEL
# ==========================================

class Role(
    AuditBaseModel
):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    code = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return self.name