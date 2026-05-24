from django.db import models

from django.conf import settings


# =========================================
# AUDIT BASE MODEL
# =========================================

class AuditBaseModel(
    models.Model
):

    # =====================================
    # STATUS
    # =====================================

    is_active = models.BooleanField(
        default=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    # =====================================
    # TIMESTAMPS
    # =====================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # =====================================
    # AUDIT
    # =====================================

    created_by = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        null=True,

        blank=True,

        on_delete=models.SET_NULL,

        related_name="+"
    )

    updated_by = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        null=True,

        blank=True,

        on_delete=models.SET_NULL,

        related_name="+"
    )

    class Meta:

        abstract = True


# =========================================
# SCHOOL BASE MODEL
# =========================================

class SchoolBaseModel(
    AuditBaseModel
):

    school = models.ForeignKey(

        "schools.School",

        on_delete=models.CASCADE,

        related_name="%(class)s_objects",

        null=True,

        blank=True
    )

    class Meta:

        abstract = True