from django.db import models
from django.core.exceptions import ValidationError


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            # Normalize name before saving
            self.name = self.name.strip().title()   # "   physics " → "Physics"
        super().save(*args, **kwargs)

    def clean(self):
        # Extra safeguard: prevent duplicates ignoring case
        if Subject.objects.exclude(pk=self.pk).filter(name__iexact=self.name).exists():
            from django.core.exceptions import ValidationError
            raise ValidationError({"name": "This subject already exists (case-insensitive)."})



class ClassSubject(models.Model):
    subject_class = models.ForeignKey("Class", on_delete=models.CASCADE, related_name="class_subjects")
        # Stream is optional for lower classes
    stream = models.ForeignKey(
        "Stream", on_delete=models.SET_NULL, null=True, blank=True, related_name="stream_subjects"
    )

    SUB_STREAM_CHOICES = [
        ("Medical", "Medical"),
        ("Non-Medical", "Non-Medical"),
        ("Vocational", "Vocational"),
    ]

    sub_stream = models.CharField(max_length=100, choices=SUB_STREAM_CHOICES, null=True, blank=True) 
    # e.g. "Medical", "Non-Medical" (simple text, no separate table unless needed)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, related_name="class_subjects")
    # Period allocations
    theory_periods_per_week = models.PositiveIntegerField(default=0)
    practical_periods_per_week = models.PositiveIntegerField(default=0)

    periods_per_week = models.PositiveIntegerField(default=0)
    is_optional = models.BooleanField(default=False)
    has_lab = models.BooleanField(default=False)
    #subject is shared across multiple classes or streams
    is_shared = models.BooleanField(default=False) 
    class Meta:
        unique_together = ("subject_class", "stream", "sub_stream", "subject")


    def clean(self):
        # Validation: If has_lab is True, ensure practical periods > 0
        if self.has_lab and self.practical_periods_per_week == 0:
            raise ValidationError("Subjects with a lab must have practical_periods_per_week > 0.")

    def save(self, *args, **kwargs):
        # Auto-calculate total periods
        self.periods_per_week = self.theory_periods_per_week + self.practical_periods_per_week
        super().save(*args, **kwargs)

    def __str__(self):
        parts = [str(self.subject_class)]

        if self.stream:
            parts.append(str(self.stream))

        if self.sub_stream:
            parts.append(str(self.sub_stream))

        parts.append(str(self.subject))

        return " - ".join(parts)