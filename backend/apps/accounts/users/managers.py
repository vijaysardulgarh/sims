from django.contrib.auth.models import (
    BaseUserManager
)

from django.db import transaction


# ==========================================
# CUSTOM USER MANAGER
# ==========================================

class UserManager(
    BaseUserManager
):

    # ======================================
    # CREATE USER
    # ======================================

    @transaction.atomic
    def create_user(

        self,

        email,

        password=None,

        **extra_fields
    ):

        if not email:

            raise ValueError(
                "User email is required."
            )

        email = self.normalize_email(
            email
        )

        # ==================================
        # DEFAULT FLAGS
        # ==================================

        extra_fields.setdefault(
            "is_active",
            True
        )

        extra_fields.setdefault(
            "is_staff",
            False
        )

        extra_fields.setdefault(
            "is_superuser",
            False
        )

        # ==================================
        # CREATE USER
        # ==================================

        user = self.model(

            email=email,

            username=email,

            **extra_fields
        )

        # ==================================
        # PASSWORD
        # ==================================

        if password:

            user.set_password(
                password
            )

        else:

            user.set_unusable_password()

        user.save(
            using=self._db
        )

        return user

    # ======================================
    # CREATE SUPERUSER
    # ======================================

    @transaction.atomic
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

        # ==================================
        # VALIDATION
        # ==================================

        if extra_fields.get(
            "is_staff"
        ) is not True:

            raise ValueError(
                "Superuser must have is_staff=True."
            )

        if extra_fields.get(
            "is_superuser"
        ) is not True:

            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self.create_user(

            email=email,

            password=password,

            **extra_fields
        )