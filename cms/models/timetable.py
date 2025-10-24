from django.db import models
from django.core.exceptions import ValidationError


class Day(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)  # e.g., Monday / Cycle Day 1
    sequence = models.PositiveIntegerField()  # ordering

    class Meta:
        unique_together = ("school", "name")
        ordering = ["sequence"]

    def __str__(self):
        return f"{self.name}"



class TimetableSlot(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    # Sequence for ordering (always present)
    sequence_number = models.PositiveIntegerField()

    # Period number only for teaching slots
    period_number = models.PositiveIntegerField(null=True, blank=True)

    start_time = models.TimeField()
    end_time = models.TimeField()

    # Flags
    is_break = models.BooleanField(default=False)
    is_assembly = models.BooleanField(default=False)
    is_special_event = models.BooleanField(default=False)

    class Meta:
        unique_together = ("school", "day", "sequence_number")
        ordering = ["day", "sequence_number"]

    def __str__(self):
        label = f"{self.day.name}"
        if self.period_number:
            label += f" (Period {self.period_number})"
        if self.is_break:
            label += " [Break]"
        if self.is_assembly:
            label += " [Assembly]"
        if self.is_special_event:
            label += " [Special Event]"
        return label

class Timetable(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE, related_name="timetable_entries")
    teacher_assignment = models.ForeignKey(
        "TeacherSubjectAssignment",
        on_delete=models.CASCADE,
        related_name="timetable_entries"
    )
    slot = models.ForeignKey("TimetableSlot", on_delete=models.CASCADE, related_name="timetable_entries")
    classroom = models.ForeignKey("Classroom", on_delete=models.SET_NULL, null=True, blank=True)
    substitute_teacher = models.ForeignKey(
        "Staff", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="substitute_entries",
        limit_choices_to={"staff_role": "Teaching"}
    )

    class Meta:
        unique_together = [
            ('teacher_assignment', 'slot'),
            ('classroom', 'slot'),
        ]
        ordering = ["slot__day", "slot__period_number"]

    def clean(self):
        super().clean()
        if Timetable.objects.filter(
            teacher_assignment__section=self.teacher_assignment.section,
            slot=self.slot
        ).exclude(id=self.id).exists():
            raise ValidationError("This section already has a subject assigned in this slot.")

    def __str__(self):
        return f"{self.teacher_assignment.teacher.name} → {self.teacher_assignment.class_subject.subject.name} @ {self.slot}"

    @property
    def teacher(self):
        return self.teacher_assignment.teacher

    @property
    def section(self):
        return self.teacher_assignment.section

    @property
    def class_subject(self):
        return self.teacher_assignment.class_subject
    