from django.db import models

from django.core.exceptions import (
    ValidationError
)

from django.db.models.functions import (
    Lower
)


# =========================================
# SUBJECT
# =========================================

class Subject(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        db_index=True
    )

    name = models.CharField(
        max_length=100,
        db_index=True
    )

    class Meta:

        db_table = "subjects"

        ordering = ["name"]

        constraints = [

            models.UniqueConstraint(

                Lower("name"),

                "school",

                name="unique_subject_per_school_case_insensitive"
            )
        ]

    def clean(self):

        if Subject.objects.exclude(
            pk=self.pk
        ).filter(

            school=self.school,

            name__iexact=self.name

        ).exists():

            raise ValidationError({
                "name":
                "This subject already exists."
            })

    def save(self, *args, **kwargs):

        if self.name:
            self.name = (
                self.name.strip().title()
            )

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name


# =========================================
# CLASS SUBJECT
# =========================================

class ClassSubject(models.Model):

    class_obj = models.ForeignKey(
        "Class",
        on_delete=models.CASCADE,
        related_name="class_subjects",
        db_index=True
    )

    stream = models.ForeignKey(
        "Stream",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stream_subjects",
        db_index=True
    )

    subject = models.ForeignKey(
        "Subject",
        on_delete=models.CASCADE,
        related_name="class_subjects",
        db_index=True
    )

    sub_stream = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    theory_periods_per_week = (
        models.PositiveIntegerField(default=0)
    )

    practical_periods_per_week = (
        models.PositiveIntegerField(default=0)
    )

    periods_per_week = (
        models.PositiveIntegerField(default=0)
    )

    is_optional = models.BooleanField(
        default=False
    )

    has_lab = models.BooleanField(
        default=False
    )

    is_shared = models.BooleanField(
        default=False
    )

    def save(self, *args, **kwargs):

        self.periods_per_week = (

            self.theory_periods_per_week +

            self.practical_periods_per_week
        )

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.subject.name}"
            f" ({self.class_obj})"
        )