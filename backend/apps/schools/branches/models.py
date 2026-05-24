from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


# ==========================================
# BRANCH MODEL
# ==========================================

class Branch(
    SchoolBaseModel
):

    name = models.CharField(
        max_length=255
    )

    code = models.CharField(
        max_length=50
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    # ======================================
    # STRING
    # ======================================

    def __str__(
        self
    ):

        return self.name

    # ======================================
    # META
    # ======================================

    class Meta:

        ordering = [
            "name"
        ]

        indexes = [

            models.Index(
                fields=["school"]
            ),

            models.Index(
                fields=["is_active"]
            ),

            models.Index(
                fields=["is_deleted"]
            ),
        ]

        unique_together = (
            "school",
            "code"
        )