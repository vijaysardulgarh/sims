from django.db import models

from apps.core.common.base.models import (
    AuditBaseModel
)


# ==========================================
# PERMISSION MODEL
# ==========================================

class Permission(
    AuditBaseModel
):

    # ======================================
    # BASIC INFO
    # ======================================

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

    # ======================================
    # SYSTEM
    # ======================================

    is_system_permission = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:

        ordering = [
            "module",
            "display_order",
            "name"
        ]

        indexes = [

            models.Index(fields=["module"]),

            models.Index(fields=["code"]),
        ]

    def __str__(self):

        return self.name