from django.contrib.auth.models import (
    AbstractUser
)

from django.core.exceptions import (
    ValidationError
)

from django.db import models

from apps.core.models import (
    AuditBaseModel
)

from apps.users.models.user_manager import (
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


    # =====================================
    # EXTRA FIELDS
    # =====================================

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

    last_password_changed_at = (
        models.DateTimeField(
            null=True,
            blank=True
        )
    )


    # =====================================
    # VALIDATION
    # =====================================

    def clean(self):

        if not self.email:

            raise ValidationError(
                "Email is required"
            )


    # =====================================
    # SAVE
    # =====================================

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

        self.full_clean()

        super().save(
            *args,
            **kwargs
        )


    # =====================================
    # STRING
    # =====================================

    def __str__(self):

        return self.email


    # =====================================
    # META
    # =====================================

    class Meta:

        indexes = [
            models.Index(
                fields=["email"]
            ),
        ]

        ordering = [
            "email"
        ]