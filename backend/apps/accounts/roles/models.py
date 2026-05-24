from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)



# ==========================================
# ROLE MODEL
# ==========================================

class Role(
    SchoolBaseModel
):

    name = models.CharField(
        max_length=100
    )

    code = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_system_role = models.BooleanField(
        default=False
    )

    class Meta:

        unique_together = [

            ("school", "name"),

            ("school", "code"),
        ]

        ordering = [
            "name"
        ]

    def __str__(self):

        return self.name