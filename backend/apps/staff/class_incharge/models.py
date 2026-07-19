from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError

from apps.academics.sections.models import Section
from apps.staff.profiles.models import Staff
from apps.core.common.base.models import SchoolBaseModel


class ClassIncharge(SchoolBaseModel):
    """
    Stores current and historical Class Incharge assignments.
    """

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="class_incharges",
    )

    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name="class_incharge_assignments",
        limit_choices_to={
            "staff_role": "Teaching",
            "is_active": True,
        },
    )

    assigned_date = models.DateField(
        auto_now_add=True
    )

    effective_from = models.DateField()

    effective_to = models.DateField(
        null=True,
        blank=True,
    )

    active = models.BooleanField(
        default=True
    )

    remarks = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = "Class Incharge"
        verbose_name_plural = "Class Incharges"

        ordering = [
            "section__class_obj__display_order",
            "section__name",
        ]

        constraints = [

            # Only one active class incharge per section
            models.UniqueConstraint(
                fields=["section"],
                condition=Q(active=True),
                name="unique_active_incharge_per_section",
            ),

            # A teacher can be class incharge of only one active section
            models.UniqueConstraint(
                fields=["staff"],
                condition=Q(active=True),
                name="unique_active_section_per_teacher",
            ),
        ]

    def clean(self):

        if (
            self.effective_to
            and self.effective_to < self.effective_from
        ):
            raise ValidationError({
                "effective_to":
                    "Effective To must be after Effective From."
            })

        if self.staff.staff_role != "Teaching":
            raise ValidationError({
                "staff":
                    "Only teaching staff can be assigned as Class Incharge."
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        status = "Active" if self.active else "Inactive"
        return f"{self.section} → {self.staff.name} ({status})"