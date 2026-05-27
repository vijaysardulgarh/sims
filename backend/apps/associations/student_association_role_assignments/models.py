# =============================================================================
# student_association_role_assignments/models.py
# =============================================================================

from django.db import models

from django.core.exceptions import (
    ValidationError
)

from apps.students.profiles.models import (
    Student
)

from apps.associations.association_roles.models import (
    AssociationRole
)

from apps.core.common.base.models import (
    SchoolBaseModel
)


class StudentAssociationRoleAssignment(
    SchoolBaseModel
):

    academic_session = models.ForeignKey(

        "academics.AcademicSession",

        on_delete=models.CASCADE,

        related_name=
        "student_association_role_assignments",

        db_index=True
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="association_roles",

        db_index=True
    )

    role = models.ForeignKey(

        AssociationRole,

        on_delete=models.CASCADE,

        related_name="assigned_students",

        db_index=True
    )

    class Meta:

        verbose_name = (
            "Student Role Assignment"
        )

        verbose_name_plural = (
            "Student Role Assignments"
        )

        constraints = [

            models.UniqueConstraint(

                fields=[

                    "academic_session",

                    "student",

                    "role"
                ],

                name=
                "unique_student_role_session"
            )
        ]

    def clean(self):

        if (

            self.student.school !=

            self.role.association.school
        ):

            raise ValidationError(

                "Student must belong "
                "to same school"
            )

    def __str__(self):

        return (

            f"{self.student.full_name_aadhar} - "

            f"{self.role.title}"
        )