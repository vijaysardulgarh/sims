from django.db import models

from apps.core.models import (
    AuditBaseModel
)


# ==========================================
# ACCESS CONTROL MODEL
# ==========================================

class AccessControl(
    AuditBaseModel
):

    name = models.CharField(
        max_length=255
    )

    code = models.CharField(
        max_length=255,
        unique=True
    )

    module = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return self.name