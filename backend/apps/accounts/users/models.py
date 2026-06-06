from django.contrib.auth.models import (
    AbstractUser
)

from django.core.exceptions import (
    ValidationError
)

from django.db import models

from apps.core.common.base.models import (
    AuditBaseModel
)

from apps.accounts.users.managers import (
    UserManager
)


# ==========================================
# USER MODEL
# ==========================================

class User(
    AbstractUser,
    AuditBaseModel
):

    objects = UserManager()

    # ======================================
    # AUTH
    # ======================================

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

    # ======================================
    # PROFILE
    # ======================================

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

    # ======================================
    # VERIFICATION
    # ======================================

    is_email_verified = models.BooleanField(
        default=False
    )

    is_phone_verified = models.BooleanField(
        default=False
    )

    # ======================================
    # SECURITY
    # ======================================

    last_password_changed_at = (
        models.DateTimeField(
            null=True,
            blank=True
        )
    )

    # ======================================
    # VALIDATION
    # ======================================

    def clean(
        self
    ):

        if not self.email:

            raise ValidationError(
                "Email is required."
            )

    # ======================================
    # SAVE
    # ======================================

    def save(
        self,
        *args,
        **kwargs
    ):

        if self.email:

            self.email = (
                self.email
                .lower()
                .strip()
            )

        if not self.username:

            self.username = self.email

        super().save(
            *args,
            **kwargs
        )

    # ======================================
    # FULL NAME
    # ======================================

    @property
    def full_name(
        self
    ):

        return (
            f"{self.first_name} "
            f"{self.last_name}"
        ).strip()

    # ======================================
    # STRING
    # ======================================

    def __str__(
        self
    ):

        return self.email

    # ======================================
    # META
    # ======================================

    class Meta:

        ordering = [
            "email"
        ]

        indexes = [

            models.Index(
                fields=["email"]
            ),

            models.Index(
                fields=["is_deleted"]
            ),
        ]