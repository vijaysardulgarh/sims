from django.db import models
from django.db.models import Q

from apps.core.common.base.models import AuditBaseModel
from apps.core.utils.slug import generate_unique_slug


class Cluster(AuditBaseModel):

    # ======================================
    # BASIC INFORMATION
    # ======================================

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Cluster Name",
    )

    code = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique Cluster Code",
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
        help_text="Brief description of the cluster",
    )

    # ======================================
    # CRC INFORMATION
    # ======================================

    crc_name = models.CharField(
        max_length=255,
        help_text="CRC Coordinator/Incharge Name",
    )

    crc_designation = models.CharField(
        max_length=100,
        blank=True,
        help_text="CRC Coordinator Designation",
    )

    crc_phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="CRC Mobile Number",
    )

    crc_email = models.EmailField(
        blank=True,
        null=True,
        help_text="CRC Email Address",
    )

    # ======================================
    # OFFICE CONTACT INFORMATION
    # ======================================

    email = models.EmailField(
        blank=True,
        null=True,
        help_text="Official Cluster Email",
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Official Cluster Contact Number",
    )

    address = models.TextField(
        blank=True,
        help_text="Cluster Office Address",
    )

    # ======================================
    # STATUS
    # ======================================

    is_active = models.BooleanField(
        default=True,
    )

    # ======================================
    # SAVE
    # ======================================

    def save(self, *args, **kwargs):

        self.name = self.name.strip()
        self.code = self.code.strip().upper()

        if self.crc_name:
            self.crc_name = self.crc_name.strip()

        if self.crc_designation:
            self.crc_designation = self.crc_designation.strip()

        if not self.slug:
            self.slug = generate_unique_slug(
                Cluster,
                self.name,
            )

        super().save(*args, **kwargs)

    # ======================================
    # STRING REPRESENTATION
    # ======================================

    def __str__(self):
        return f"{self.code} - {self.name}"

    # ======================================
    # META
    # ======================================

    class Meta:

        db_table = "clusters"

        verbose_name = "Cluster"

        verbose_name_plural = "Clusters"

        ordering = [
            "name",
        ]

        constraints = [

            models.UniqueConstraint(
                fields=["email"],
                condition=Q(email__isnull=False),
                name="unique_cluster_email_if_present",
            ),

            models.UniqueConstraint(
                fields=["crc_email"],
                condition=Q(crc_email__isnull=False),
                name="unique_crc_email_if_present",
            ),

        ]

        indexes = [

            models.Index(fields=["is_active"]),
            models.Index(fields=["is_deleted"]),

        ]