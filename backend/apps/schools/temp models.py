from django.db import models

from django.db.models import Q

from django.core.exceptions import (
    ValidationError
)

from apps.core.common.base.models import (
    AuditBaseModel
)

from apps.core.utils.slug import (
    generate_unique_slug
)

from apps.clusters.models import Cluster
# ==========================================
# SCHOOL LOGO PATH
# ==========================================

def school_logo_path(
    instance,
    filename
):

    slug = (
        instance.slug
        or "unassigned"
    )

    return (
        f"schools/{slug}/logo/{filename}"
    )




# ==========================================
# SCHOOL MODEL
# ==========================================

class School(
    AuditBaseModel
):

    # ======================================
    # CHOICES
    # ======================================

    SCHOOL_TYPE_CHOICES = [

        ("PRIMARY", "Primary School"),

        ("MIDDLE", "Middle School"),

        (
            "SECONDARY",
            "Secondary School"
        ),

        (
            "SENIOR_SECONDARY",
            "Senior Secondary School"
        ),

        ("K12", "K-12 School"),

        ("COLLEGE", "College"),

        (
            "COACHING",
            "Coaching Institute"
        ),
    ]

    BOARD_CHOICES = [

        ("CBSE", "CBSE"),

        ("ICSE", "ICSE"),

        (
            "STATE",
            "State Board"
        ),

        (
            "IB",
            "International Baccalaureate"
        ),

        (
            "CAMBRIDGE",
            "Cambridge"
        ),

        ("OTHER", "Other"),
    ]

    # ======================================
    # RELATIONS
    # ======================================

    cluster = models.ForeignKey(

        Cluster,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="schools"
    )

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

    subdomain = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    motto = models.CharField(
        max_length=255,
        blank=True
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
        upload_to=school_logo_path,
        blank=True,
        null=True,
        default="schools/default/logo.png"
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

    alternate_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True,
        null=True
    )

    # ======================================
    # ADDRESS
    # ======================================

    address = models.TextField(
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    state = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    country = models.CharField(
        max_length=100,
        default="India"
    )

    pincode = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    # ======================================
    # MANAGEMENT
    # ======================================

    principal_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    established_date = (
        models.DateField(
            blank=True,
            null=True
        )
    )

    accreditation = models.CharField(
        max_length=255,
        blank=True
    )

    affiliation_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # ======================================
    # ACADEMICS
    # ======================================

    school_type = models.CharField(
        max_length=50,
        choices=SCHOOL_TYPE_CHOICES,
        blank=True,
        null=True
    )

    board = models.CharField(
        max_length=50,
        choices=BOARD_CHOICES,
        blank=True,
        null=True
    )

    language = models.CharField(
        max_length=50,
        default="English"
    )

    academic_year_start_month = (
        models.PositiveIntegerField(
            default=4
        )
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
    # SOCIAL
    # ======================================

    social_media_links = models.JSONField(
        default=dict,
        blank=True
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
    # VALIDATION
    # ======================================

    def clean(
        self
    ):

        if self.established_date:

            from datetime import date

            if (

                self.established_date
                > date.today()
            ):

                raise ValidationError(

                    (
                        "Established date "
                        "cannot be in future."
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
                    School,
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

        verbose_name = "School"

        verbose_name_plural = "Schools"

        ordering = [
            "name"
        ]

        constraints = [

            models.UniqueConstraint(

                models.functions.Lower(
                    "name"
                ),

                name=(
                    "unique_school_name_case_insensitive"
                )
            ),

            models.UniqueConstraint(

                fields=["email"],

                condition=Q(
                    email__isnull=False
                ),

                name=(
                    "unique_school_email_if_present"
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
                fields=["subdomain"]
            ),

            models.Index(
                fields=["is_active"]
            ),

            models.Index(
                fields=["is_deleted"]
            ),
        ]