from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from apps.schools.models import School


# =========================
# CLASS
# =========================
class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classes", db_index=True)
    name = models.CharField(max_length=50)
    class_order = models.PositiveIntegerField(default=0)

    def clean(self):
        if self.name:
            self.name = self.name.strip().upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "name"], name="unique_class_per_school")
        ]
        ordering = ["class_order", "name"]

    def __str__(self):
        return self.name


# =========================
# STREAM
# =========================
class Stream(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="streams", db_index=True)

    def clean(self):
        if self.name:
            self.name = self.name.strip().upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "name"], name="unique_stream_per_school")
        ]

    def __str__(self):
        return self.name


# =========================
# MEDIUM
# =========================
class Medium(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="mediums", db_index=True)

    def clean(self):
        if self.name:
            self.name = self.name.strip().upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "name"], name="unique_medium_per_school")
        ]

    def __str__(self):
        return self.name


# =========================
# CLASSROOM
# =========================
class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classrooms", db_index=True)
    name = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField(default=40)
    floor = models.CharField(max_length=20, blank=True, null=True)

    def clean(self):
        if self.name:
            self.name = self.name.strip().upper()

        if self.capacity <= 0:
            raise ValidationError("Capacity must be greater than 0")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "name"], name="unique_classroom_per_school")
        ]

    def __str__(self):
        return f"Room {self.name}"


# =========================
# SECTION
# =========================
class Section(models.Model):

    SUB_STREAM_CHOICES = [
        ("Medical", "Medical"),
        ("Non-Medical", "Non-Medical"),
        ("Vocational", "Vocational"),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="sections", db_index=True)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="sections", db_index=True)
    name = models.CharField(max_length=10)

    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name="sections")
    medium = models.ForeignKey(Medium, on_delete=models.SET_NULL, null=True, blank=True, related_name="sections")
    stream = models.ForeignKey(Stream, on_delete=models.SET_NULL, null=True, blank=True, related_name="sections")

    sub_stream = models.CharField(max_length=100, choices=SUB_STREAM_CHOICES, null=True, blank=True)

    def clean(self):

        if self.name:
            self.name = self.name.strip().upper()

        if self.sub_stream and not self.stream:
            raise ValidationError("Sub-stream requires a stream")

        if self.class_obj and self.class_obj.school != self.school:
            raise ValidationError("Class must belong to the same school")

        if self.stream and self.stream.school != self.school:
            raise ValidationError("Stream must belong to the same school")

        if self.medium and self.medium.school != self.school:
            raise ValidationError("Medium must belong to the same school")

        if self.classroom and self.classroom.school != self.school:
            raise ValidationError("Classroom must belong to the same school")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["school", "class_obj", "name"],
                condition=Q(stream__isnull=True, medium__isnull=True, sub_stream__isnull=True),
                name="unique_section_basic"
            ),

            models.UniqueConstraint(
                fields=["school", "class_obj", "name", "stream"],
                condition=Q(stream__isnull=False, sub_stream__isnull=True),
                name="unique_section_stream_only"
            ),

            models.UniqueConstraint(
                fields=["school", "class_obj", "name", "stream", "sub_stream"],
                condition=Q(stream__isnull=False, sub_stream__isnull=False),
                name="unique_section_substream"
            ),

            models.UniqueConstraint(
                fields=["school", "class_obj", "name", "medium"],
                condition=Q(stream__isnull=True, medium__isnull=False, sub_stream__isnull=True),
                name="unique_section_medium"
            ),

            # 🔥 FINAL ADDITION
            models.CheckConstraint(
                check=Q(sub_stream__isnull=True) | Q(stream__isnull=False),
                name="substream_requires_stream"
            ),
        ]

        indexes = [
            models.Index(fields=["school", "class_obj"]),
            models.Index(fields=["school", "name"]),
            models.Index(fields=["school", "stream"]),
            models.Index(fields=["school", "medium"]),
            models.Index(fields=["class_obj", "name"]),
        ]

        ordering = ["class_obj__class_order", "name"]

    def __str__(self):
        base = f"{self.class_obj.name} {self.name}"

        if self.stream:
            base += f" ({self.stream.name})"
        if self.sub_stream:
            base += f" - {self.sub_stream}"
        if self.medium:
            base += f" - {self.medium.name}"

        return base
    


    
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower


# -----------------------------------------------------------------------------
# SUBJECT
# -----------------------------------------------------------------------------

class Subject(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        db_table = "subjects"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                Lower("name"), "school",
                name="unique_subject_per_school_case_insensitive"
            )
        ]

    def clean(self):
        if Subject.objects.exclude(pk=self.pk).filter(
            school=self.school,
            name__iexact=self.name
        ).exists():
            raise ValidationError({"name": "This subject already exists for this school."})

    def save(self, *args, **kwargs):
        # 🔥 Normalize here (correct place)
        if self.name:
            self.name = self.name.strip().title()

        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.school})"


# -----------------------------------------------------------------------------
# CLASS SUBJECT
# -----------------------------------------------------------------------------

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

    SUB_STREAM_CHOICES = [
        ("Medical", "Medical"),
        ("Non-Medical", "Non-Medical"),
        ("Vocational", "Vocational"),
    ]

    sub_stream = models.CharField(
        max_length=100,
        choices=SUB_STREAM_CHOICES,
        null=True,
        blank=True,
        db_index=True
    )

    subject = models.ForeignKey(
        "Subject",
        on_delete=models.CASCADE,
        related_name="class_subjects",
        db_index=True
    )

    theory_periods_per_week = models.PositiveIntegerField(default=0)
    practical_periods_per_week = models.PositiveIntegerField(default=0)
    periods_per_week = models.PositiveIntegerField(default=0)

    is_optional = models.BooleanField(default=False)
    has_lab = models.BooleanField(default=False)
    is_shared = models.BooleanField(default=False)

    class Meta:
        db_table = "class_subjects"
        ordering = ["id"]  # 🔥 avoid join-heavy ordering

        constraints = [
            models.UniqueConstraint(
                fields=["class_obj", "stream", "sub_stream", "subject"],
                name="unique_class_subject_mapping"
            ),

            models.CheckConstraint(
                check=models.Q(theory_periods_per_week__gte=0),
                name="theory_periods_non_negative"
            ),
            models.CheckConstraint(
                check=models.Q(practical_periods_per_week__gte=0),
                name="practical_periods_non_negative"
            ),

            models.CheckConstraint(
                check=models.Q(theory_periods_per_week__gt=0) | models.Q(practical_periods_per_week__gt=0),
                name="at_least_one_period"
            ),

            models.CheckConstraint(
                check=models.Q(sub_stream__in=["Medical", "Non-Medical", "Vocational"]) | models.Q(sub_stream__isnull=True),
                name="valid_sub_stream"
            ),

            # 🔥 Lab constraint at DB level
            models.CheckConstraint(
                check=(
                    models.Q(has_lab=False) |
                    models.Q(practical_periods_per_week__gt=0)
                ),
                name="lab_requires_practical"
            ),
        ]

        indexes = [
            models.Index(fields=["class_obj", "stream"]),
            models.Index(fields=["class_obj", "subject"]),
            models.Index(fields=["class_obj", "stream", "subject"]),
        ]

    def clean(self):

        if self.subject.school != self.class_obj.school:
            raise ValidationError("Subject must belong to same school as class.")

        if self.stream and self.stream.school != self.class_obj.school:
            raise ValidationError("Stream must belong to same school.")

        if self.stream and self.stream.class_obj != self.class_obj:
            raise ValidationError("Stream must belong to selected class.")

        if self.sub_stream and not self.stream:
            raise ValidationError("Sub-stream requires stream.")

        if self.has_lab and self.practical_periods_per_week == 0:
            raise ValidationError("Lab subject must have practical periods.")

        if self.practical_periods_per_week > 0 and not self.has_lab:
            raise ValidationError("Practical requires has_lab=True.")

        total = self.theory_periods_per_week + self.practical_periods_per_week

        if total == 0:
            raise ValidationError("At least one period required.")

        if self.is_optional and total > 6:
            raise ValidationError("Optional subject cannot have too many periods.")

    def save(self, *args, **kwargs):
        self.periods_per_week = self.theory_periods_per_week + self.practical_periods_per_week
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject.name} ({self.class_obj})"    
    

from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q


# -----------------------------------------------------------------------------
# DAY
# -----------------------------------------------------------------------------

class Day(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=20)  # e.g., Monday / Cycle Day 1
    sequence = models.PositiveIntegerField()

    class Meta:
        db_table = "days"
        ordering = ["sequence"]
        constraints = [
            models.UniqueConstraint(fields=["school", "name"], name="unique_day_per_school"),
            models.UniqueConstraint(fields=["school", "sequence"], name="unique_day_sequence_per_school"),
        ]

    def __str__(self):
        return self.name


# -----------------------------------------------------------------------------
# TIMETABLE SLOT
# -----------------------------------------------------------------------------

class TimetableSlot(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE, db_index=True)
    day = models.ForeignKey("Day", on_delete=models.CASCADE, db_index=True)

    sequence_number = models.PositiveIntegerField()
    period_number = models.PositiveIntegerField(null=True, blank=True)

    start_time = models.TimeField()
    end_time = models.TimeField()

    is_break = models.BooleanField(default=False)
    is_assembly = models.BooleanField(default=False)
    is_special_event = models.BooleanField(default=False)

    class Meta:
        db_table = "timetable_slots"
        ordering = ["day", "sequence_number"]

        constraints = [
            models.UniqueConstraint(
                fields=["school", "day", "sequence_number"],
                name="unique_slot_sequence_per_day"
            ),

            # Ensure period_number is unique per day (only for teaching slots)
            models.UniqueConstraint(
                fields=["school", "day", "period_number"],
                condition=Q(period_number__isnull=False),
                name="unique_period_per_day"
            ),

            # Time must be valid
            models.CheckConstraint(
                check=Q(start_time__lt=models.F("end_time")),
                name="valid_time_range"
            ),
        ]

        indexes = [
            models.Index(fields=["school", "day"]),
        ]

    def clean(self):
        # Cross-school validation
        if self.day.school != self.school:
            raise ValidationError("Day must belong to the same school.")

        # Only one type allowed
        flags = [self.is_break, self.is_assembly, self.is_special_event]
        if sum(flags) > 1:
            raise ValidationError("A slot cannot be multiple types (break/assembly/event).")

        # Special slots must not have period_number
        if (self.is_break or self.is_assembly or self.is_special_event) and self.period_number:
            raise ValidationError("Special slots cannot have a period number.")

        # Teaching slot must have period_number
        if not (self.is_break or self.is_assembly or self.is_special_event):
            if not self.period_number:
                raise ValidationError("Teaching slot must have a period number.")

        # Time overlap validation
        overlapping = TimetableSlot.objects.filter(
            school=self.school,
            day=self.day,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError("This time slot overlaps with an existing slot.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        label = f"{self.day.name}"

        if self.period_number:
            label += f" (Period {self.period_number})"

        if self.is_break:
            label += " [Break]"
        elif self.is_assembly:
            label += " [Assembly]"
        elif self.is_special_event:
            label += " [Special Event]"

        return label


# -----------------------------------------------------------------------------
# TIMETABLE ENTRY
# -----------------------------------------------------------------------------

class Timetable(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE, related_name="timetable_entries", db_index=True)

    teacher_subject_assignment = models.ForeignKey(
        "TeacherSubjectAssignment",
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        db_index=True
    )

    slot = models.ForeignKey(
        "TimetableSlot",
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        db_index=True
    )

    classroom = models.ForeignKey(
        "Classroom",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True
    )

    substitute_teacher = models.ForeignKey(
        "Staff",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="substitute_entries",
        limit_choices_to={"staff_role": "Teaching"},
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "timetable_entries"
        ordering = ["slot__day", "slot__sequence_number"]

        constraints = [
            # Teacher cannot be in two places at same time
            models.UniqueConstraint(
                fields=["teacher_subject_assignment", "slot"],
                name="unique_teacher_slot"
            ),

            # Classroom cannot be double booked
            models.UniqueConstraint(
                fields=["classroom", "slot"],
                condition=Q(classroom__isnull=False),
                name="unique_classroom_slot"
            ),
        ]

        indexes = [
            models.Index(fields=["slot"]),
            models.Index(fields=["teacher_subject_assignment"]),
        ]

    def clean(self):
        # Cross-school safety
        if self.teacher_subject_assignment.school != self.school:
            raise ValidationError("Assignment must belong to same school.")

        if self.slot.school != self.school:
            raise ValidationError("Slot must belong to same school.")

        if self.classroom and self.classroom.school != self.school:
            raise ValidationError("Classroom must belong to same school.")

        # Section conflict (only one subject per section per slot)
        if Timetable.objects.filter(
            teacher_subject_assignment__section=self.teacher_subject_assignment.section,
            slot=self.slot
        ).exclude(pk=self.pk).exists():
            raise ValidationError("This section already has a subject in this slot.")

        # Teacher conflict (extra safety)
        if Timetable.objects.filter(
            teacher_subject_assignment__teacher=self.teacher_subject_assignment.teacher,
            slot=self.slot
        ).exclude(pk=self.pk).exists():
            raise ValidationError("Teacher is already assigned in this slot.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.teacher_subject_assignment.teacher.name} → "
            f"{self.teacher_subject_assignment.class_subject.subject.name} @ {self.slot}"
        )

    @property
    def teacher(self):
        return self.teacher_subject_assignment.teacher

    @property
    def section(self):
        return self.teacher_subject_assignment.section

    @property
    def class_subject(self):
        return self.teacher_subject_assignment.class_subject    