from django.db import models


class AuditBaseModel(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    created_by = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    updated_by = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        abstract = True


class SchoolBaseModel(AuditBaseModel):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True