# =============================================================================
# associations/models/association_member.py
# =============================================================================

from django.db import models
from django.core.exceptions import ValidationError

from apps.staff.profiles.models import Staff
from apps.students.profiles.models import Student

from apps.associations.associations.models import (
    Association
)

from apps.core.common.base.models import (
    SessionBaseModel
)


class AssociationMember(
    SessionBaseModel
):

    STAFF = "STAFF"
    STUDENT = "STUDENT"
    EXTERNAL = "EXTERNAL"

    MEMBER_TYPE_CHOICES = [

        (STAFF, "Staff"),

        (STUDENT, "Student"),

        (EXTERNAL, "External"),

    ]

    association = models.ForeignKey(

        Association,

        on_delete=models.CASCADE,

        related_name="members"
    )

    member_type = models.CharField(

        max_length=20,

        choices=MEMBER_TYPE_CHOICES,

        db_index=True
    )

    # Internal Members

    staff = models.ForeignKey(

        Staff,

        on_delete=models.CASCADE,

        null=True,

        blank=True,

        related_name="association_memberships"
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        null=True,

        blank=True,

        related_name="association_memberships"
    )

    # External Member Details

    external_name = models.CharField(

        max_length=255,

        blank=True
    )

    external_email = models.EmailField(

        blank=True
    )

    external_phone_number = models.CharField(

        max_length=15,

        blank=True
    )

    external_designation = models.CharField(

        max_length=255,

        blank=True
    )

    image = models.ImageField(

        upload_to="association_members/",

        blank=True
    )

    class Meta:

        verbose_name = (
            "Association Member"
        )

        verbose_name_plural = (
            "Association Members"
        )

        ordering = [
            "member_type"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "academic_session",
                    "association",
                    "staff"
                ],

                name=
                "unique_staff_association_member"
            ),

            models.UniqueConstraint(

                fields=[
                    "academic_session",
                    "association",
                    "student"
                ],

                name=
                "unique_student_association_member"
            ),
        ]

    def clean(self):

        if self.member_type == self.STAFF:

            if not self.staff:

                raise ValidationError(
                    "Staff is required."
                )

            if self.student:

                raise ValidationError(
                    "Student must be empty."
                )

            if (
                self.staff.school !=
                self.association.school
            ):
                raise ValidationError(
                    "Staff must belong to same school."
                )

        elif self.member_type == self.STUDENT:

            if not self.student:

                raise ValidationError(
                    "Student is required."
                )

            if self.staff:

                raise ValidationError(
                    "Staff must be empty."
                )

            if (
                self.student.school !=
                self.association.school
            ):
                raise ValidationError(
                    "Student must belong to same school."
                )

        elif self.member_type == self.EXTERNAL:

            if not self.external_name:

                raise ValidationError(
                    "External name is required."
                )

            if self.staff or self.student:

                raise ValidationError(
                    "External members cannot have staff or student."
                )

    @property
    def member_name(self):

        if self.staff:
            return self.staff.name

        if self.student:
            return self.student.full_name

        return self.external_name

    def __str__(self):

        return (
            f"{self.member_name}"
            f" - "
            f"{self.association.name}"
        )