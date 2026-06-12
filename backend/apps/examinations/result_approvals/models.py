from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.examinations.result_generations.models import (
    ResultGeneration,
)
from apps.accounts.users.models import User

class ResultApproval(
    SessionBaseModel
):

    STATUS_CHOICES = [

        ("PENDING", "Pending"),

        ("APPROVED", "Approved"),

        ("REJECTED", "Rejected"),
    ]

    result = models.OneToOneField(

        ResultGeneration,

        on_delete=models.CASCADE,

        related_name="approval",
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="PENDING",
    )

    approved_by = models.ForeignKey(

        User,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="approved_results",
    )

    approved_at = models.DateTimeField(

        null=True,

        blank=True,
    )

    rejection_reason = models.TextField(
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "result_approvals"
        )

        ordering = [
            "-created_at",
        ]

    def __str__(self):

        return (
            f"{self.result}"
        )