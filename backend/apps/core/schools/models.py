from django.db import models


class School(models.Model):

    name = models.CharField(
        max_length=255
    )

    code = models.CharField(
        max_length=50,
        unique=True
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

    website = models.URLField(
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    principal_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    timezone = models.CharField(
        max_length=100,
        default="Asia/Kolkata"
    )

    currency = models.CharField(
        max_length=20,
        default="INR"
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.name