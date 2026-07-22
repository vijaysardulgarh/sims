from django.core.exceptions import ValidationError
from django.db import models
from apps.academics.classes.models import Class      
from apps.academics.sections.models import Section
from apps.core.common.base.models import SessionBaseModel
from apps.academics.subjects.models import Subject
from apps.academics.streams.models import Stream


class SubjectRequirement(SessionBaseModel):
    school_class = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="subject_requirements",
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="subject_requirements",
        null=True,
        blank=True,
    )
    stream = models.ForeignKey(
        Stream,
        on_delete=models.SET_NULL,
        related_name="subject_requirements",
        null=True,
        blank=True,
    )
    sub_stream = models.CharField(
        max_length=100,
        blank=True,
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="subject_requirements",
    )
    theory_periods_per_week = models.PositiveIntegerField(
        default=0,
    )
    lab_periods_per_week = models.PositiveIntegerField(
        default=0,
    )
    is_compulsory = models.BooleanField(
        default=True,
    )
    is_shared = models.BooleanField(
        default=False,
        help_text="Subject is shared between multiple classes/sections.",
    )
    priority = models.PositiveIntegerField(
        default=0,
        help_text="Priority for timetabling/scheduling.",
    )
    teachers_required = models.PositiveIntegerField(
        default=1,
        help_text="Number of teachers required for this subject requirement.",
    )
    remarks = models.TextField(
        blank=True,
    )

    @property
    def total_periods_per_week(self):
        return self.theory_periods_per_week + self.lab_periods_per_week

    @property
    def requires_lab(self):
        return self.lab_periods_per_week > 0

    def clean(self):
        super().clean()

        if self.theory_periods_per_week == 0 and self.lab_periods_per_week == 0:
            raise ValidationError(
                "At least one theory or lab period must be greater than zero."
            )

        # Expanded list to accommodate common variations of senior class names
        senior_classes = ["11", "12", "11TH", "12TH", "ELEVENTH", "TWELFTH", "XI", "XII"]

        if self.stream and not any(grade in self.school_class.name.upper() for grade in senior_classes):
            raise ValidationError(
                {
                    "stream": "Streams are allowed only for senior classes."
                }
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        parts = [str(self.school_class)]

        if self.section:
            parts.append(str(self.section))
        if self.stream:
            parts.append(self.stream.name)
        if self.sub_stream:
            parts.append(self.sub_stream)

        parts.append(self.subject.name)
        return " - ".join(parts)

    class Meta:
        db_table = "tt_subject_requirements"
        ordering = [
            "school_class__display_order",
            "subject__name",
        ]
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "school",
                    "academic_session",
                    "school_class",
                    "section",
                    "stream",
                    "sub_stream",
                    "subject",
                ],
                name="unique_subject_requirement",
            ),
        ]
        indexes = [
            models.Index(
                fields=[
                    "school",
                    "academic_session",
                    "school_class",
                ]
            ),
            models.Index(fields=["stream"]),
            models.Index(fields=["subject"]),
        ]