from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager
)

from django.core.exceptions import ValidationError

from django.db import models

from apps.core.models import AuditBaseModel
from apps.schools.models import School

# ==========================================
# CUSTOM USER MANAGER
# ==========================================

class UserManager(BaseUserManager):

    def create_user(
        self,
        email,
        password=None,
        **extra_fields
    ):

        if not email:

            raise ValueError(
                "Email is required"
            )

        email = self.normalize_email(
            email
        )

        user = self.model(
            email=email,
            username=email,
            **extra_fields
        )

        user.set_password(password)

        user.save(
            using=self._db
        )

        return user

    def create_superuser(
        self,
        email,
        password=None,
        **extra_fields
    ):

        extra_fields.setdefault(
            "is_staff",
            True
        )

        extra_fields.setdefault(
            "is_superuser",
            True
        )

        extra_fields.setdefault(
            "is_active",
            True
        )

        return self.create_user(
            email,
            password,
            **extra_fields
        )


# ==========================================
# USER MODEL
# ==========================================

class User(AbstractUser, AuditBaseModel):

    objects = UserManager()

    username = models.CharField(
        max_length=150,
        blank=True,
        unique=True
    )

    email = models.EmailField(
        unique=True,
        db_index=True
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    # ------------------------------------------
    # EXTRA FIELDS
    # ------------------------------------------

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    profile_photo = models.ImageField(
        upload_to="users/photos/",
        blank=True,
        null=True
    )

    designation = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    is_email_verified = models.BooleanField(
        default=False
    )

    is_phone_verified = models.BooleanField(
        default=False
    )

    last_password_changed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    # ------------------------------------------
    # VALIDATION
    # ------------------------------------------

    def clean(self):

        if not self.email:

            raise ValidationError(
                "Email is required"
            )

    # ------------------------------------------
    # SAVE
    # ------------------------------------------

    def save(self, *args, **kwargs):

        if self.email:

            self.email = (
                self.email
                .lower()
                .strip()
            )

        if not self.username:

            self.username = self.email

        self.full_clean()

        super().save(
            *args,
            **kwargs
        )

    # ------------------------------------------
    # STRING
    # ------------------------------------------

    def __str__(self):

        school_name = (
            self.school.name
            if self.school
            else "No School"
        )

        return (
            f"{self.email} "
            f"({school_name})"
        )

    # ------------------------------------------
    # META
    # ------------------------------------------

    class Meta:

        indexes = [
            models.Index(fields=["email"]),
        ]

        ordering = [
            "email"
        ]


# ==========================================
# ROLE MODEL
# ==========================================

class Role(AuditBaseModel):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    code = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return self.name


# ==========================================
# PERMISSION MODEL
# ==========================================

class Permission(AuditBaseModel):

    name = models.CharField(
        max_length=255
    )

    code = models.CharField(
        max_length=255,
        unique=True
    )

    module = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return self.name


# ==========================================
# USER ROLE MODEL
# ==========================================

class UserRole(AuditBaseModel):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_roles"
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="user_roles"
    )

    class Meta:

        unique_together = (
            "user",
            "role",
        )

    def __str__(self):

        return (
            f"{self.user.email} - "
            f"{self.role.name}"
        )


# ==========================================
# ROLE PERMISSION MODEL
# ==========================================

class RolePermission(AuditBaseModel):

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="role_permissions"
    )

    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        related_name="role_permissions"
    )

    class Meta:

        unique_together = (
            "role",
            "permission"
        )

    def __str__(self):

        return (
            f"{self.role.name} - "
            f"{self.permission.code}"
        )