from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):

    # Username optional but must NOT be NULL
    username = models.CharField(max_length=150, blank=True, unique=True)

    # Email is login field
    email = models.EmailField(unique=True, db_index=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    ROLE_CHOICES = [
        ("principal", "Principal"),
        ("teacher", "Teacher"),
        ("clerk", "Clerk"),
        ("student", "Student"),
        ("admin", "Admin"),
    ]

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default="teacher",
        db_index=True
    )

    school = models.ForeignKey(
        "School",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users",
        db_index=True
    )

    staff = models.OneToOneField(
        "Staff",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user"
    )

    student = models.OneToOneField(
        "Student",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user"
    )

    # -------------------------
    # VALIDATION
    # -------------------------
    def clean(self):

        if not self.email:
            raise ValidationError("Email is required")

        # Superuser handling
        if self.is_superuser:
            self.role = "admin"
            if self.staff and self.student:
                raise ValidationError("User cannot be both staff and student")
            return

        if not self.school:
            raise ValidationError("School is required for all users")

        if self.role in ["teacher", "principal", "clerk"] and not self.staff:
            raise ValidationError(f"{self.role} user must be linked to staff")

        if self.role == "student" and not self.student:
            raise ValidationError("Student user must be linked to student")

        if self.role == "admin" and (self.staff or self.student):
            raise ValidationError("Admin should not be linked to staff or student")

        if self.staff and self.student:
            raise ValidationError("User cannot be both staff and student")

        if self.staff and self.role == "student":
            raise ValidationError("Student role cannot be linked to staff")

        if self.student and self.role != "student":
            raise ValidationError("Only student role can link to student")

        if self.staff and self.school != self.staff.school:
            raise ValidationError("User school must match staff school")

        if self.student and self.school != self.student.school:
            raise ValidationError("User school must match student school")

    # -------------------------
    # SAVE
    # -------------------------
    def save(self, *args, **kwargs):

        # Normalize email
        if self.email:
            self.email = self.email.lower().strip()

        # Ensure username always exists and normalized
        if not self.username:
            self.username = self.email
        else:
            self.username = self.username.lower().strip()

        # Deterministic admin access
        self.is_staff = bool(self.is_superuser or self.role in ["admin", "principal"])

        self.full_clean()
        super().save(*args, **kwargs)

    # -------------------------
    # STRING
    # -------------------------
    def __str__(self):
        school_name = self.school.name if self.school else "No School"
        return f"{self.email} ({school_name} - {self.role})"

    # -------------------------
    # META
    # -------------------------
    class Meta:
        indexes = [
            models.Index(fields=["role"]),
            models.Index(fields=["school"]),
            models.Index(fields=["email"]),
        ]
        ordering = ["school", "role", "email"]