from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q

from apps.staff.post_type.models import PostType
from apps.schools.models import School

class Staff(models.Model):

    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        OTHER = "Other", "Other"

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="staff"
    )

    employee_id = models.CharField(
        max_length=20,
        db_index=True
    )

    name = models.CharField(
        max_length=50,
        db_index=True
    )

    post_type = models.ForeignKey(
        PostType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.name} ({self.employee_id})"

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["school", "employee_id"],
                name="unique_employee_per_school"
            )
        ]