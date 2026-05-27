from django.db import models

from django.db.models import Q

from apps.core.common.base.models import (
    AuditBaseModel
)

from apps.core.utils.slug import (
    generate_unique_slug
)
# ==========================================
# CLUSTER LOGO PATH
# ==========================================

def cluster_logo_path(
    instance,
    filename
):

    slug = (
        instance.slug
        or "unassigned"
    )

    return (
        f"clusters/{slug}/logo/{filename}"
    )


# ==========================================
# CLUSTER MODEL
# ==========================================

class Cluster(
    AuditBaseModel
):

    # ======================================
    # BASIC INFO
    # ======================================

    name = models.CharField(
        max_length=255,
        db_index=True
    )

    code = models.CharField(
        max_length=50,
        unique=True
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    # ======================================
    # STATUS
    # ======================================

    is_active = models.BooleanField(
        default=True
    )

    # ======================================
    # MEDIA
    # ======================================

    logo = models.ImageField(
        upload_to=cluster_logo_path,
        blank=True,
        null=True
    )

    # ======================================
    # CONTACT
    # ======================================

    email = models.EmailField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    # ======================================
    # REGION
    # ======================================

    timezone = models.CharField(
        max_length=100,
        default="Asia/Kolkata"
    )

    currency = models.CharField(
        max_length=20,
        default="INR"
    )

    # ======================================
    # GPS
    # ======================================

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    geo_radius_meters = (
        models.PositiveIntegerField(
            default=100,
            help_text=(
                "Geofence radius in meters"
            )
        )
    )

    # ======================================
    # SAVE
    # ======================================

    def save(
        self,
        *args,
        **kwargs
    ):

        if not self.slug:

            self.slug = (
                generate_unique_slug(
                    Cluster,
                    self.name
                )
            )

        self.full_clean()

        super().save(
            *args,
            **kwargs
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

        verbose_name = "Cluster"

        verbose_name_plural = "Clusters"

        ordering = [
            "name"
        ]

        constraints = [

            models.UniqueConstraint(

                models.functions.Lower(
                    "name"
                ),

                name=(
                    "unique_cluster_name_case_insensitive"
                )
            ),

            models.UniqueConstraint(

                fields=["email"],

                condition=Q(
                    email__isnull=False
                ),

                name=(
                    "unique_cluster_email_if_present"
                )
            ),
        ]

        indexes = [

            models.Index(
                fields=["name"]
            ),

            models.Index(
                fields=["code"]
            ),

            models.Index(
                fields=["is_active"]
            ),

            models.Index(
                fields=["is_deleted"]
            ),
        ]

