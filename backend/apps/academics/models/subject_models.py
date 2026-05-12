from django.db import models

from django.core.exceptions import ValidationError

from django.db.models.functions import Lower
from .class_models import Section


# =========================================
# SUBJECT
# =========================================

class Subject(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="subjects",
        db_index=True
    )

    name = models.CharField(
        max_length=100,
        db_index=True
    )

    code = models.CharField(
        max_length=20,
        blank=True,
        null=True
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

        if self.code:
            self.code = (
                self.code.strip().upper()
            )

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name


# =========================================
# CLASS SUBJECT
# =========================================

class ClassSubject(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="class_subjects",
        db_index=True
    )

    class_obj = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="class_subjects",
        db_index=True
    )

    stream = models.ForeignKey(
        "academics.Stream",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stream_subjects",
        db_index=True
    )

    subject = models.ForeignKey(
        "academics.Subject",
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

    class Meta:

        db_table = "class_subjects"

        ordering = [
            "class_obj__class_order",
            "subject__name"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "class_obj",
                    "stream",
                    "subject",
                    "sub_stream"
                ],

                name="unique_class_subject"
            )
        ]

    def clean(self):

        # Prevent invalid periods
        if (
            self.theory_periods_per_week < 0 or
            self.practical_periods_per_week < 0
        ):
            raise ValidationError(
                "Periods cannot be negative."
            )

        # Auto validation
        total = (
            self.theory_periods_per_week +
            self.practical_periods_per_week
        )

        if total <= 0:
            raise ValidationError(
                "Total periods must be greater than 0."
            )

        # Stream validation
        senior_classes = [
            "11TH",
            "12TH",
            "ELEVENTH",
            "TWELFTH"
        ]

        if self.stream and (
            self.class_obj.name.upper()
            not in senior_classes
        ):
            raise ValidationError({
                "stream":
                "Streams are allowed only for senior classes."
            })

    def save(self, *args, **kwargs):

        self.periods_per_week = (

            self.theory_periods_per_week +

            self.practical_periods_per_week
        )

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        parts = [
            self.subject.name,
            f"({self.class_obj})"
        ]

        if self.stream:
            parts.append(self.stream.name)

        if self.sub_stream:
            parts.append(self.sub_stream)

        return " - ".join(parts)
    

# =========================
# 🔹 TEACHER SUBJECT ASSIGNMENT
# =========================
class TeacherSubjectAssignment(models.Model):

    teacher = models.ForeignKey(
        "staff.Staff",
        on_delete=models.CASCADE,
        related_name="subject_assignments",
        limit_choices_to={"staff_role": "Teaching"}
    )
    

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="subject_assignments"
    )

    class_subject = models.ForeignKey(
        "academics.ClassSubject",
        on_delete=models.CASCADE,
        related_name="teacher_assignments"
    )

    def clean(self):
        if self.teacher.school != self.section.school:
            raise ValidationError("Teacher and Section must belong to same school")

        if self.class_subject.school != self.section.school:
            raise ValidationError("ClassSubject must belong to same school")

        total = TeacherSubjectAssignment.objects.filter(
            teacher=self.teacher
        ).exclude(pk=self.pk).count()

        if total >= self.teacher.max_periods_per_week:
            raise ValidationError("Teacher exceeded max workload")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.teacher.name} → {self.section}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["teacher", "section", "class_subject"],
                name="unique_teacher_section_subject"
            )
        ]
        indexes = [
            models.Index(fields=["section"]),
            models.Index(fields=["teacher"]),
        ]    