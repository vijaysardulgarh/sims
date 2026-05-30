# =============================================================================
# associations/models/smc_member.py
# =============================================================================

from django.db import models

from apps.core.common.base.models import SessionBaseModel


class SMCMember(SessionBaseModel):

    POSITION_CHOICES = [
        ("President", "President"),
        ("Vice President", "Vice President"),
        ("Member (Secretary)", "Member (Secretary)"),
        (
            "Member (Trained Education Scholar)",
            "Member (Trained Education Scholar)"
        ),
        (
            "Member (Teacher/Student)",
            "Member (Teacher/Student)"
        ),
        (
            "Member (Parent/Guardian)",
            "Member (Parent/Guardian)"
        ),
        (
            "Member (General)",
            "Member (General)"
        ),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    CATEGORY_CHOICES = [
        ("GEN", "General"),
        ("SC", "Scheduled Caste"),
        ("BC-A", "Backward Class - A"),
        ("BC-B", "Backward Class - B"),
        ("EWS", "Economically Weaker Section"),
        ("OTHER", "Other"),
    ]

    # ============================================
    # BASIC DETAILS
    # ============================================

    name = models.CharField(
        max_length=100
    )

    position = models.CharField(
        max_length=100,
        choices=POSITION_CHOICES
    )

    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        blank=True,
        null=True
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

    address = models.TextField(
        blank=True
    )

    # ============================================
    # TENURE DETAILS
    # ============================================

    nomination_date = models.DateField(
        blank=True,
        null=True
    )

    tenure_end_date = models.DateField(
        blank=True,
        null=True
    )

    # ============================================
    # MEDIA
    # ============================================

    photo = models.ImageField(
        upload_to="smc_photos/",
        blank=True,
        null=True
    )

    # ============================================
    # DISPLAY SETTINGS
    # ============================================

    priority = models.PositiveIntegerField(
        default=0
    )

    show_on_website = models.BooleanField(
        default=True
    )

    # ============================================
    # NOTES
    # ============================================

    remarks = models.TextField(
        blank=True
    )

    # ============================================
    # META
    # ============================================

    class Meta:

        verbose_name = "SMC Member"
        verbose_name_plural = "SMC Members"

        ordering = [
            "priority",
            "name",
        ]

    # ============================================
    # STRING REPRESENTATION
    # ============================================

    def __str__(self):

        return (
            f"{self.name} - "
            f"{self.position}"
        )