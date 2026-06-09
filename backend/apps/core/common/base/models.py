from django.db import models
from django.conf import settings


# =============================================================================
# AUDIT BASE MODEL
# =============================================================================

class AuditBaseModel(
    models.Model
):

    # =========================================================================
    # STATUS
    # =========================================================================

    is_active = models.BooleanField(
        default=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    # =========================================================================
    # TIMESTAMPS
    # =========================================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # =========================================================================
    # AUDIT USERS
    # =========================================================================

    created_by = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="+"
    )

    updated_by = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="+"
    )

    class Meta:

        abstract = True
# =============================================================================
# CLUSTER BASE MODEL                    
# =============================================================================
class ClusterBaseModel(
    AuditBaseModel
):

    cluster = models.ForeignKey(

        "clusters.Cluster",

        on_delete=models.CASCADE,

        related_name="%(class)s_objects",

        db_index=True,

        null=True,

        blank=True
    )

    class Meta:

        abstract = True
# =============================================================================
# SCHOOL BASE MODEL
# =============================================================================

class SchoolBaseModel(
    AuditBaseModel
):

    school = models.ForeignKey(

        "schools.School",

        on_delete=models.CASCADE,

        related_name="%(class)s_objects",

        db_index=True,

        null=True,

        blank=True
    )

    class Meta:

        abstract = True


# =============================================================================
# SESSION BASE MODEL
# =============================================================================

class SessionBaseModel(
    SchoolBaseModel
):

    academic_session = models.ForeignKey(

        "academics.AcademicSession",

        on_delete=models.CASCADE,

        related_name="%(class)s_objects",

        db_index=True,

        null=True,

        blank=True
    )

    class Meta:

        abstract = True


class PublishableBaseModel(
    models.Model
):

    is_published = models.BooleanField(
        default=False
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

class OrderedBaseModel(
    models.Model
):

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        abstract = True                