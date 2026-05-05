from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from .school import School
from .classes import Section


# =========================
# 🔹 POST TYPE
# =========================
class PostType(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., TGT, PGT
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# =========================
# 🔹 STAFF
# =========================
class Staff(models.Model):

    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        OTHER = "Other", "Other"

    class StaffRole(models.TextChoices):
        ADMIN = "Administrative", "Administrative"
        TEACHING = "Teaching", "Teaching"
        NON_TEACHING = "Non-Teaching", "Non-Teaching"
        SUPPORT = "Support", "Support"

    class EmploymentType(models.TextChoices):
        REGULAR = "Regular", "Regular"
        SSA = "SSA", "SSA"
        GUEST = "Guest", "Guest"
        HKRNL = "HKRNL", "HKRNL"
        NSQF = "NSQF", "NSQF"
        MDM = "MDMWorker", "MDM Worker"
        OTHER = "Other", "Other"

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="staff")

    employee_id = models.CharField(max_length=20, db_index=True)
    name = models.CharField(max_length=50, db_index=True)

    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    spouse_name = models.CharField(max_length=50, blank=True, null=True)

    gender = models.CharField(max_length=6, choices=Gender.choices, blank=True, null=True)

    aadhar_number = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        help_text="Optional. Must be unique if provided."
    )

    post_type = models.ForeignKey(PostType, on_delete=models.SET_NULL, null=True, blank=True)

    category = models.CharField(max_length=50, blank=True, null=True)

    date_of_birth = models.DateField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    current_joining_date = models.DateField(null=True, blank=True)
    retirement_date = models.DateField(null=True, blank=True)

    qualification = models.CharField(max_length=255, blank=True, null=True)

    subject = models.ForeignKey(
        "Subject",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="staff_subjects"
    )

    email = models.EmailField(blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True, db_index=True)

    profile_picture = models.ImageField(
        upload_to="staff_profile/",
        null=True,
        blank=True,
        default="staff_profile/default.png"
    )

    staff_role = models.CharField(
        max_length=20,
        choices=StaffRole.choices,
        default=StaffRole.TEACHING
    )

    employment_type = models.CharField(
        max_length=20,
        choices=EmploymentType.choices,
        default=EmploymentType.REGULAR
    )

    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True, db_index=True)
    is_deleted = models.BooleanField(default=False)

    priority = models.PositiveIntegerField(default=0)
    max_periods_per_week = models.PositiveIntegerField(default=40)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.subject and self.subject.school != self.school:
            raise ValidationError("Subject must belong to same school")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"

    class Meta:
        verbose_name_plural = "Staff"

        ordering = ["school", "post_type", "name"]

        constraints = [
            models.UniqueConstraint(
                fields=["school", "employee_id"],
                name="unique_employee_per_school"
            ),
            models.UniqueConstraint(
                fields=["aadhar_number"],
                condition=Q(aadhar_number__isnull=False),
                name="unique_aadhar_if_present"
            ),
            models.UniqueConstraint(
                fields=["email"],
                condition=Q(email__isnull=False),
                name="unique_email_if_present"
            ),
        ]

        indexes = [
            models.Index(fields=["school", "staff_role"]),
            models.Index(fields=["school", "employee_id"]),
            models.Index(fields=["school", "is_active"]),
        ]


# =========================
# 🔹 CLASS INCHARGE
# =========================
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
        limit_choices_to={"staff_role": "Teaching"},
    )

    assigned_date = models.DateField(auto_now_add=True)
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)

    active = models.BooleanField(default=True)

    def clean(self):
        if self.staff.staff_role != "Teaching":
            raise ValidationError("Only teaching staff allowed")

        if self.staff.school != self.section.school:
            raise ValidationError("Staff and Section must belong to same school")

        overlapping = ClassIncharge.objects.filter(
            section=self.section,
            active=True
        ).exclude(pk=self.pk).filter(
            Q(effective_to__isnull=True) | Q(effective_to__gte=self.effective_from)
        )

        if overlapping.exists():
            raise ValidationError("Overlapping incharge assignment exists")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

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


# =========================
# 🔹 SANCTIONED POSTS
# =========================
class SanctionedPost(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="sanctioned_posts"
    )

    post_type = models.ForeignKey(PostType, on_delete=models.SET_NULL, null=True, blank=True)

    designation = models.CharField(max_length=50, blank=True, null=True)

    subject = models.ForeignKey(
        "Subject",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    total_posts = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.school} - {self.post_type} ({self.total_posts})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["school", "post_type", "designation", "subject"],
                name="unique_sanctioned_post"
            )
        ]


# =========================
# 🔹 TEACHER SUBJECT ASSIGNMENT
# =========================
class TeacherSubjectAssignment(models.Model):

    teacher = models.ForeignKey(
        Staff,
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
        "ClassSubject",
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


# =========================
# 🔹 TEACHER ATTENDANCE
# =========================
class TeacherAttendance(models.Model):

    school = models.ForeignKey(School, on_delete=models.CASCADE)

    teacher = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        limit_choices_to={"staff_role": "Teaching"}
    )

    date = models.DateField()
    present = models.BooleanField(default=True)

    def clean(self):
        if self.teacher.school != self.school:
            raise ValidationError("Teacher must belong to same school")

    def __str__(self):
        return f"{self.teacher.name} - {self.date}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["school", "teacher", "date"],
                name="unique_teacher_attendance_per_day"
            )
        ]
        indexes = [
            models.Index(fields=["school", "date"]),
            models.Index(fields=["teacher", "date"]),
        ]