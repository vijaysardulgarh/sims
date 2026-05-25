from django.db import models

from apps.core.common.base.models import (
    AuditBaseModel
)

from apps.accounts.modules.models import (
    Module
)


# ==========================================
# PERMISSION MODEL
# ==========================================

class Permission(
    AuditBaseModel
):

    ACTION_CHOICES = [

        ("view", "View"),

        ("add", "Add"),

        ("edit", "Edit"),

        ("delete", "Delete"),

        ("import", "Import"),

        ("export", "Export"),

        ("assign", "Assign"),

        ("approve", "Approve"),
    ]

    # ======================================
    # MODULE
    # ======================================

    module = models.ForeignKey(

        Module,

        on_delete=models.CASCADE,

        related_name="permissions",
    )

    # ======================================
    # ACTION
    # ======================================

    action = models.CharField(

        max_length=50,

        choices=ACTION_CHOICES,
    )

    # ======================================
    # AUTO GENERATED
    # ======================================

    name = models.CharField(

        max_length=255,

        editable=False,
    )

    code = models.CharField(

        max_length=255,

        unique=True,

        editable=False,
    )

    # ======================================
    # OPTIONAL
    # ======================================

    description = models.TextField(

        blank=True,

        null=True,
    )

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

        unique_together = (
            "module",
            "action",
        )

    def save(
        self,
        *args,
        **kwargs
    ):

        # ==================================
        # AUTO NAME
        # ==================================

        self.name = (

            f"{self.get_action_display()} "

            f"{self.module.name}"
        )

        # ==================================
        # AUTO CODE
        # ==================================

        self.code = (

            f"{self.module.slug}_"

            f"{self.action}"
        )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):

        return self.name