# =============================================================================
# associations/models/smc_member.py
# =============================================================================

from django.db import models

from apps.core.common.base.models import SessionBaseModel


class SMCMember(SessionBaseModel):

    POSITION_CHOICES = [
        ("President", "President"),
        ("Vice President", "Vice President"),
        ("Member Secretary", "Member Secretary"),
        ("Member", "Member"),
    ]


    name = models.CharField(max_length=100)

    position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES
    )

    contact_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    priority = models.PositiveIntegerField(default=0)

    show_on_website = models.BooleanField(default=True)

    class Meta:
        verbose_name = "SMC Member"
        verbose_name_plural = "SMC Members"

        ordering = [
            "priority",
            "name"
        ]

    def __str__(self):

        return f"{self.name} - {self.position}"