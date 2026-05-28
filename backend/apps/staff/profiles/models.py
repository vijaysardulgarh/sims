from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.conf import settings

from apps.staff.post_type.models import PostType
from apps.core.common.base.models import SchoolBaseModel


class Staff(SchoolBaseModel):

    # ============================================
    # USER
    # ============================================

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="staff_profile"
    )

    # ============================================
    # CHOICES
    # ============================================

    class Gender(models.TextChoices):

        MALE = "Male", "Male"

        FEMALE = "Female", "Female"

        OTHER = "Other", "Other"

    class StaffRole(models.TextChoices):

        TEACHING = "Teaching", "Teaching"

        NON_TEACHING = (
            "Non Teaching",
            "Non Teaching"
        )

        ADMIN = "Admin", "Admin"

        SUPPORT = "Support", "Support"

    class EmploymentType(models.TextChoices):

        REGULAR = "Regular", "Regular"

        CONTRACT = "Contract", "Contract"

        GUEST = "Guest", "Guest"

        PART_TIME = "Part Time", "Part Time"

    # ============================================
    # BASIC INFORMATION
    # ============================================

    employee_id = models.CharField(
        max_length=20,
        db_index=True
    )

    name = models.CharField(
        max_length=100,
        db_index=True
    )

    profile_picture = models.ImageField(
        upload_to="staff/profile_pictures/",
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        blank=True
    )

    # ============================================
    # FAMILY INFORMATION
    # ============================================

    father_name = models.CharField(
        max_length=100,
        blank=True
    )

    mother_name = models.CharField(
        max_length=100,
        blank=True
    )

    spouse_name = models.CharField(
        max_length=100,
        blank=True
    )

    # ============================================
    # EMPLOYMENT INFORMATION
    # ============================================

    post_type = models.ForeignKey(
        PostType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    staff_role = models.CharField(
        max_length=30,
        choices=StaffRole.choices,
        default=StaffRole.TEACHING
    )

    employment_type = models.CharField(
        max_length=30,
        choices=EmploymentType.choices,
        blank=True
    )

    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    qualification = models.CharField(
        max_length=255,
        blank=True
    )

    priority = models.PositiveIntegerField(
        default=1
    )

    max_periods_per_week = models.PositiveIntegerField(
        default=40
    )

    # ============================================
    # IDENTITY & CONTACT
    # ============================================

    aadhar_number = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    mobile_number = models.CharField(
        max_length=15,
        blank=True
    )

    # ============================================
    # DATES
    # ============================================

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    joining_date = models.DateField(
        null=True,
        blank=True
    )

    current_joining_date = models.DateField(
        null=True,
        blank=True
    )

    retirement_date = models.DateField(
        null=True,
        blank=True
    )

    # ============================================
    # OTHER INFORMATION
    # ============================================

    category = models.CharField(
        max_length=50,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    # ============================================
    # VALIDATIONS
    # ============================================

    def clean(self):

        if (
            self.mobile_number and
            len(self.mobile_number) < 10
        ):

            raise ValidationError({
                "mobile_number":
                "Enter valid mobile number."
            })

    # ============================================
    # STRING REPRESENTATION
    # ============================================

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.employee_id})"
        )

    # ============================================
    # META
    # ============================================

    class Meta:

        ordering = [
            "name"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "employee_id"
                ],
                name="unique_employee_per_school"
            )
        ]