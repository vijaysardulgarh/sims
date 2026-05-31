from django.db import models
from django.db.models import Q

from apps.core.common.base.models import AuditBaseModel
from apps.clusters.models import Cluster

from apps.core.utils.slug import generate_unique_slug


class School(AuditBaseModel):

    SCHOOL_TYPE_CHOICES = [
        ("PRIMARY", "Primary School"),
        ("MIDDLE", "Middle School"),
        ("SECONDARY", "Secondary School"),
        ("SENIOR_SECONDARY", "Senior Secondary School"),
        ("K12", "K-12 School"),
        ("COLLEGE", "College"),
        ("COACHING", "Coaching Institute"),
    ]

    BOARD_CHOICES = [
        ("CBSE", "CBSE"),
        ("ICSE", "ICSE"),
        ("STATE", "State Board"),
        ("IB", "International Baccalaureate"),
        ("CAMBRIDGE", "Cambridge"),
        ("OTHER", "Other"),
    ]

    SCHOOL_CATEGORY_CHOICES = [
        ("GOVERNMENT", "Government"),
        ("PRIVATE", "Private"),
        ("AIDED", "Aided"),
        ("UNAIDED", "Unaided"),
        ("PM_SHRI", "PM SHRI"),
        ("KV", "Kendriya Vidyalaya"),
        ("JNV", "Jawahar Navodaya Vidyalaya"),
        ("OTHER", "Other"),
    ]

    cluster = models.ForeignKey(
        Cluster,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="schools"
    )

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

    udise_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True
    )

    school_category = models.CharField(
        max_length=30,
        choices=SCHOOL_CATEGORY_CHOICES,
        blank=True,
        null=True
    )

    motto = models.CharField(
        max_length=255,
        blank=True
    )

    logo = models.ImageField(
        upload_to="schools/logos/",
        blank=True,
        null=True
    )

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

    principal_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    established_date = models.DateField(
        blank=True,
        null=True
    )

    affiliation_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

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

    medium_of_instruction = models.CharField(
        max_length=50,
        default="English"
    )

    timezone = models.CharField(
        max_length=100,
        default="Asia/Kolkata"
    )

    currency = models.CharField(
        max_length=20,
        default="INR"
    )

    social_media_links = models.JSONField(
        default=dict,
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = generate_unique_slug(
                School,
                self.name
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:

        ordering = ["name"]

        constraints = [

            models.UniqueConstraint(
                models.functions.Lower("name"),
                name="unique_school_name_case_insensitive"
            ),

            models.UniqueConstraint(
                fields=["email"],
                condition=Q(email__isnull=False),
                name="unique_school_email_if_present"
            ),
        ]