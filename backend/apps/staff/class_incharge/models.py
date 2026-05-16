from django.db import models
from django.db.models import Q

from apps.academics.sections.models import Section
from apps.staff.staff.models import Staff


class ClassIncharge(models.Model):

    section = models.OneToOneField(
        Section,
        on_delete=models.CASCADE,
        related_name="incharge"
    )

    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name="incharge_assignments",
        limit_choices_to={
            "staff_role": "Teaching"
        },
    )

    assigned_date = models.DateField(
        auto_now_add=True
    )

    effective_from = models.DateField()

    effective_to = models.DateField(
        null=True,
        blank=True
    )

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.staff.name} → {self.section}"

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=["section"],
                condition=Q(active=True),
                name="unique_active_incharge_per_section"
            )
        ]