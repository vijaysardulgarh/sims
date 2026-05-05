from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from .utils import generate_unique_slug


# =========================
# 🔹 FILE PATH
# =========================
def school_logo_path(instance, filename):
    slug = instance.slug or "unassigned"
    return f"schools/{slug}/logo/{filename}"


# =========================
# 🔹 SCHOOL MODEL
# =========================
class School(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    address = models.TextField(blank=True)

    website = models.URLField(blank=True)

    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)

    logo = models.ImageField(
        upload_to=school_logo_path,
        blank=True,
        null=True,
        default="schools/default/logo.png"   # ⚠️ ensure this file exists
    )

    accreditation = models.CharField(max_length=255, blank=True)
    established_date = models.DateField(null=True, blank=True)

    motto = models.CharField(max_length=255, blank=True)

    social_media_links = models.JSONField(default=dict, blank=True)

    slug = models.SlugField(unique=True, blank=True)

    is_active = models.BooleanField(default=True, db_index=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # =========================
    # 🔹 VALIDATIONS
    # =========================
    def clean(self):
        if self.established_date:
            from datetime import date
            if self.established_date > date.today():
                raise ValidationError("Established date cannot be in the future")

    # =========================
    # 🔹 SAVE
    # =========================
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(School, self.name)
        self.full_clean()   # ✅ enforce validations
        super().save(*args, **kwargs)

    # =========================
    # 🔹 STRING
    # =========================
    def __str__(self):
        return self.name

    # =========================
    # 🔹 META
    # =========================
    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
        ordering = ["name"]

        constraints = [
            # ✅ Prevent duplicate names (case-insensitive)
            models.UniqueConstraint(
                models.functions.Lower("name"),
                name="unique_school_name_case_insensitive"
            ),

            # ✅ Unique email only if provided
            models.UniqueConstraint(
                fields=["email"],
                condition=Q(email__isnull=False),
                name="unique_school_email_if_present"
            ),
        ]

        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["is_active"]),
        ]