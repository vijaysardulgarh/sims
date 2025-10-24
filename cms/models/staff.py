from django.db import models
from .school import School
from .schoolclass import Section

class PostType(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., TGT, PGT, Non-Teaching
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Staff(models.Model):

    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True, blank=True, related_name='staff')
    employee_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    mother_name = models.CharField(max_length=50, null=True, blank=True)
    spouse_name = models.CharField(max_length=50, null=True, blank=True)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    aadhar_number = models.CharField(max_length=12, unique=True, null=True, blank=True, help_text="Optional. Must be unique if provided.")
    post_type = models.ForeignKey(
        PostType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    CATEGORY_CHOICES = [
        ('GEN', 'General'),
        ('SC', 'SC'),
        ('BC-A', 'BC-A'),
        ('BC-B', 'BC-B'),
        ('EWS', 'EWS'),
        ('OTHER', 'Other'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    current_joining_date = models.DateField(null=True, blank=True)
    retirement_date = models.DateField(null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, related_name='staff_subject', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, help_text="Unique if provided")
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='staff_profile/',null=True,blank=True,default='staff_profile/default.png')

    STAFF_ROLE_CHOICES = [
        ('Administrative', 'Administrative'),
        ('Teaching', 'Teaching'),
        ('Non-Teaching', 'Non-Teaching'),
        ('Support', 'Support'),
    ]
    staff_role = models.CharField(max_length=20, choices=STAFF_ROLE_CHOICES, default='Teaching')

    EMPLOYMENT_TYPE_CHOICES = [
        ('Regular', 'Regular'),
        ('SSA', 'SSA'),
        ('Guest', 'Guest'),
        ('HKRNL', 'HKRNL'),
        ('NSQF', 'NSQF'),
        ('MDMWorker', 'MDM Worker'),
        ('Other', 'Other'),
    ]
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default='Regular')

    bio = models.TextField(blank=True)
    priority = models.PositiveIntegerField(default=0, help_text="Lower number = higher priority")
    max_periods_per_week = models.PositiveIntegerField(default=40)
    def __str__(self):
        return f"{self.name} ({self.employee_id or 'No ID'})"

    class Meta:
        unique_together = ('school', 'employee_id')    
        verbose_name_plural = "Staff"
        ordering = ["school", "post_type", "name", "staff_role", "employment_type", "priority"]


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
        limit_choices_to={"staff_role": "Teaching"},  # ✅ restrict in admin/forms
    )
    
    assigned_date = models.DateField(auto_now_add=True)  # system timestamp
    effective_from = models.DateField()                  # when the role starts
    effective_to = models.DateField(null=True, blank=True)  # when the role ends (null = still active)
    
    active = models.BooleanField(default=True)

    def clean(self):
        """Ensure only teaching staff can be assigned as class incharge."""
        if self.staff and self.staff.staff_role != "Teaching":
            from django.core.exceptions import ValidationError
            raise ValidationError(
                {"staff": "Only teaching staff can be assigned as class incharge."}
            )    
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["section"],
                condition=models.Q(active=True),
                name="unique_active_incharge_per_section"
            )
        ]

    def __str__(self):
        return f"{self.staff.name} → {self.section} [{self.effective_from} - {self.effective_to or 'Present'}]"
    


class SanctionedPost(models.Model):
    school = models.ForeignKey(
        'School',
        on_delete=models.CASCADE,
        related_name='sanctioned_posts'
    )

    post_type = models.ForeignKey(
        PostType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    designation = models.CharField(max_length=50, null=True, blank=True)  # e.g., PGT English, TGT Punjabi, Clerk
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    total_posts = models.PositiveIntegerField(default=0)

    def __str__(self):
        designation = f" {self.designation}" if self.designation else ""
        return f"{self.school} - {self.post_type}{designation} ({self.total_posts})"    
    

class TeacherSubjectAssignment(models.Model):
    teacher = models.ForeignKey(
        "Staff",
        on_delete=models.CASCADE,
        related_name="subject_assignments",
        limit_choices_to={"staff_role": "Teaching"}
    )
    section = models.ForeignKey(
        "Section",
        on_delete=models.CASCADE,
        related_name="subject_assignments"
    )
    class_subject = models.ForeignKey(
        "ClassSubject",   # Example: Class 8 – Science
        on_delete=models.CASCADE,
        related_name="teacher_assignments"
    )
    

    class Meta:
        unique_together = ("teacher", "section", "class_subject")

    def __str__(self):
        return f"{self.teacher.name} → {self.section} ({self.class_subject})"

class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(
        "Staff",
        on_delete=models.CASCADE,
        limit_choices_to={"staff_role": "Teaching"}
    )
    date = models.DateField()
    present = models.BooleanField(default=True)  # ✅ ticked by default

    class Meta:
        unique_together = ("teacher", "date")

    def __str__(self):
        return f"{self.teacher.name} - {'Present' if self.present else 'Absent'} on {self.date}"    