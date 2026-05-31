from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class MandatoryPublicDisclosure(
    SchoolBaseModel
):

    # =====================================
    # GENERAL INFORMATION
    # =====================================

    affiliation_number = models.CharField(
        max_length=100,
        blank=True
    )

    school_code = models.CharField(
        max_length=50,
        blank=True
    )

    principal_name = models.CharField(
        max_length=255,
        blank=True
    )

    principal_qualification = models.CharField(
        max_length=255,
        blank=True
    )

    school_email = models.EmailField(
        blank=True
    )

    contact_number = models.CharField(
        max_length=20,
        blank=True
    )

    # =====================================
    # STAFF DETAILS
    # =====================================

    total_teachers = models.PositiveIntegerField(
        default=0
    )

    pgt_count = models.PositiveIntegerField(
        default=0
    )

    tgt_count = models.PositiveIntegerField(
        default=0
    )

    prt_count = models.PositiveIntegerField(
        default=0
    )

    dpe_count = models.PositiveIntegerField(
        default=0
    )

    clerk_count = models.PositiveIntegerField(
        default=0
    )

    librarian_count = models.PositiveIntegerField(
        default=0
    )

    student_teacher_ratio = models.CharField(
        max_length=20,
        blank=True
    )

    special_educator_count = (
        models.PositiveIntegerField(
            default=0
        )
    )

    counsellor_count = (
        models.PositiveIntegerField(
            default=0
        )
    )

    class Meta:

        db_table = (
            "mandatory_public_disclosures"
        )

        verbose_name = (
            "Mandatory Public Disclosure"
        )

        verbose_name_plural = (
            "Mandatory Public Disclosures"
        )

        constraints = [

            models.UniqueConstraint(
                fields=["school"],
                name=(
                    "unique_mpd_per_school"
                )
            )
        ]

    def __str__(self):

        return (
            f"{self.school.name}"
        )