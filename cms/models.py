from django.db import models
from django import forms
from django.utils import timezone
import datetime
import json,os
from decimal import Decimal
#from django.contrib.gis.db import models as gis_models
from datetime import date
#from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from import_export import resources,fields
#class User(AbstractUser):
    #STUDENT = 'student'
   # TEACHER = 'teacher'
   # PARENT = 'parent'
   # ADMINISTRATOR = 'administrator'
   # STAFF = 'staff'
   # GUEST = 'guest'

   # USER_TYPE_CHOICES = [
   #     (STUDENT, 'Student'),
   #     (TEACHER, 'Teacher'),
   #     (PARENT, 'Parent/Guardian'),
   #     (ADMINISTRATOR, 'Administrator'),
   #     (STAFF, 'Staff/Non-Teaching Personnel'),
    #    (GUEST, 'Guest/User with Limited Access'),
   # ]

    #user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    #def __str__(self):
    #    return f"{self.username} - {self.get_user_type_display()}"


class School(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    address = models.TextField(blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True, db_index=True)
    phone_number = models.CharField(max_length=15, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    accreditation = models.CharField(max_length=255, blank=True)
    established_date = models.DateField(null=True, blank=True)
    motto = models.CharField(max_length=255, blank=True)

    # Location (optional, requires GeoDjango setup)
    #location = gis_models.PointField(blank=True, null=True)

    # Store social links as JSON instead of text for structure
    social_media_links = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
        ordering = ["name"]



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

    def __str__(self):
        return f"{self.name} ({self.employee_id or 'No ID'})"

    class Meta:
        unique_together = ('school', 'employee_id')    
        verbose_name_plural = "Staff"
        ordering = ["school", "priority","staff_role", "employment_type", "name"]



class Medium(models.Model):
    name = models.CharField(max_length=50)  # e.g., English, Hindi, Punjabi
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="mediums")

    class Meta:
        unique_together = ('school', 'name')

    def __str__(self):
        return f"{self.name} ({self.school.name})"
    
class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classrooms")
    room_number = models.CharField(max_length=20)   # e.g., R101, Block A-2
    capacity = models.PositiveIntegerField(default=40)
    floor = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = ('school', 'room_number')

    def __str__(self):
        return f"Room {self.room_number} ({self.school.name})"


class Stream(models.Model):

    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="streams")

    class Meta:
        unique_together = ('school', 'name')

    def __str__(self):
        return f"{self.name} ({self.school.name})"
    

class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classes")
    name = models.CharField(max_length=50)  # e.g., 9th, 10th
    stream = models.ForeignKey(Stream, on_delete=models.SET_NULL, null=True, blank=True, related_name="classes")
    medium = models.ForeignKey(Medium, on_delete=models.SET_NULL, null=True, blank=True, related_name="classes")

    class Meta:
        unique_together = ('school', 'name', 'stream', 'medium')

    def __str__(self):
        base = f"{self.name}"
        if self.stream:
            base += f" ({self.stream.name})"
        if self.medium:
            base += f" - {self.medium.name}"
        return f"{base} ({self.school.name})"

class Section(models.Model):
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="sections")
    name = models.CharField(max_length=10)  # e.g., A, B, C
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name="sections")

    class Meta:
        unique_together = ('school_class', 'name')

    def __str__(self):
        room = f" - Room {self.classroom.room_number}" if self.classroom else ""
        return f"{self.school_class.name} {self.name}{room} ({self.school_class.school.name})"

    

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
    class_info = models.ForeignKey("Class", on_delete=models.CASCADE, related_name="class_subjects")
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, related_name="class_subjects")
    periods_per_week = models.PositiveIntegerField(default=0)
    is_optional = models.BooleanField(default=False)
    has_lab = models.BooleanField(default=False)

    class Meta:
        unique_together = ("class_info", "subject")

    def __str__(self):
        return f"{self.class_info} - {self.subject}"



class Day(models.Model):
    school = models.ForeignKey("School", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)  # e.g., Monday / Cycle Day 1
    sequence = models.PositiveIntegerField()  # ordering

    class Meta:
        unique_together = ("school", "name")
        ordering = ["sequence"]

    def __str__(self):
        return f"{self.school.name} - {self.name}"



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
    section = models.ForeignKey("Section", on_delete=models.CASCADE, related_name="timetable_entries")
    class_subject = models.ForeignKey(
        "ClassSubject", 
        on_delete=models.CASCADE, 
        related_name="timetable_entries"
    )
    teacher = models.ForeignKey(
        "Staff", 
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        limit_choices_to={"staff_role": "Teaching"}
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
            ("section", "slot"),      # 1 section can't have 2 subjects at same slot
            ("teacher", "slot"),      # teacher can't be double-booked
            ("classroom", "slot"),    # classroom can't be double-booked
        ]
        ordering = ["slot__day", "slot__period_number"]

    def __str__(self):
        return f"{self.section} - {self.class_subject.subject.name} by ({self.teacher.name}) @ {self.slot}"

    def clean(self):
        # ✅ Validate teacher is actually assigned to this class_subject
        if not TeacherSubjectAssignment.objects.filter(
            teacher=self.teacher,
            class_subject=self.class_subject
        ).exists():
            raise ValidationError(
                {"teacher": f"{self.teacher.name} is not assigned to {self.class_subject}."}
            )


class TeacherSubjectAssignment(models.Model):
    teacher = models.ForeignKey(
        "Staff", 
        on_delete=models.CASCADE,
        related_name="subject_assignments",
        limit_choices_to={"staff_role": "Teaching"}
    )
    class_subject = models.ForeignKey(
        "ClassSubject", 
        on_delete=models.CASCADE, 
        related_name="teacher_assignments"
    )
    max_periods_per_week = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("teacher", "class_subject")

    def __str__(self):
        return f"{self.teacher.name} → {self.class_subject}"
        

class TimetableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        instance = kwargs.get("instance")

        # If editing an existing Timetable entry
        if instance and instance.class_name and instance.subject:
            teacher_ids = TeacherSubjectAssignment.objects.filter(
                class_subject__class_info=instance.class_name,
                class_subject__subject=instance.subject
            ).values_list("teacher_id", flat=True)

            self.fields["teachers"].queryset = Staff.objects.filter(
                id__in=teacher_ids, 
                is_teaching=True  # only teaching staff
            )

        # If adding a new entry, we can start with empty queryset
        else:
            self.fields["teachers"].queryset = Staff.objects.none()

    class Meta:
        model = Timetable
        fields = "__all__"








    


class AboutSchool(models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE, related_name='about')
    history = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)

    def __str__(self):
        return f"About {self.school.name}"

    class Meta:
        verbose_name = "About School"
        verbose_name_plural = "About Schools"



class Principal(models.Model):
    """One principal per school."""
    school = models.OneToOneField(School, on_delete=models.CASCADE, related_name='principal')
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="principal/", blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Principal {self.name} ({self.school.name})"

    class Meta:
        verbose_name = "Principal"
        verbose_name_plural = "Principals"


class Affiliation(models.Model):
    """External affiliations (like CBSE, ICSE, IB, etc.)."""
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='affiliations')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("school", "name")  # Prevent duplicate affiliations for the same school
        verbose_name = "Affiliation"
        verbose_name_plural = "Affiliations"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.school.name}"







class Facility(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="facilities")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='facility_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.school.name})"

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"
        ordering = ["name"]

# class Nodal(models.Model):
#     ROLE_CHOICES = [
#         # Academic & Curriculum
#         ('exam_nodal', 'Examination Nodal Officer'),

#         # Student Support & Welfare
#         ('discipline_nodal', 'Discipline Nodal Officer'),
#         ('health_safety', 'Health & Safety Nodal'),
#         ('counseling_nodal', 'Counseling & Guidance Nodal'),
#         ('anti_bullying', 'Anti-Bullying / Child Protection Nodal'),
#         ('cwsn', 'CWSN Nodal'),
#         ('scholarship_nodal', 'Scholarship Nodal'),

#         # ICT & Innovation
#         ('ict_nodal', 'ICT / Smart Class Nodal'),
#         ('digital_learning', 'Digital Learning Nodal'),
#         ('library_nodal', 'Library Nodal'),
#         ('innovation_nodal', 'Innovation & ATL Nodal'),

#         # Co-curricular & Cultural
#         ('sports_nodal', 'Sports Nodal Officer'),
#         ('art_culture', 'Art & Culture Nodal'),
#         ('music_dance', 'Music & Dance Nodal'),
#         ('literary_coord', 'Literary / Debate Nodal'),

#         # Govt. Schemes & Committees
#         ('middaymeal', 'Mid-Day Meal Nodal'),
#         ('rti_nodal', 'RTI Nodal Officer'),
#         ('smc_coord', 'School Management Committee Nodal'),
#         ('pocso_nodal', 'POCSO / Child Safety Nodal'),
#         ('ecoclub_nodal', 'Eco Club / Environment Nodal'),
#         ('swachhta_nodal', 'Swachhta Abhiyan Nodal'),

#         # Community & External
#         ('career_guidance', 'Career Guidance Nodal'),

#         # Admin & Infrastructure
#         ('transport_nodal', 'Transport Nodal Officer'),
#         ('property', 'Property Register Nodal'),
#         ('procurement', 'Procurement / Stores Nodal'),
#     ]

#     school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='nodal_officers')
#     staff = models.ManyToManyField('Staff', related_name='nodal_roles')
#     role = models.CharField(max_length=100, choices=ROLE_CHOICES, db_index=True)
#     responsibilities = models.TextField(blank=True)
#     bio = models.TextField(blank=True)

#     class Meta:
#         verbose_name = "Nodal Officer"
#         verbose_name_plural = "Nodal Officers"
#         unique_together = ("school", "role")  # prevent duplicate nodal role in the same school
#         ordering = ["school", "role"]

#     def __str__(self):
#         return f"{self.get_role_display()} - {self.school.name}"

# class Nodal(models.Model):
#     school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="nodals")
#     name = models.CharField(max_length=255)
#     photo = models.ImageField(upload_to="nodal_photos/", blank=True, null=True)
#     contact_number = models.CharField(max_length=20, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.name} ({self.school})"


# class Role(models.Model):
#     nodal = models.ForeignKey(Nodal, on_delete=models.CASCADE, related_name="roles")
#     title = models.CharField(max_length=255)
#     responsibilities = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.title} - {self.nodal.name}"    
class AssociationType(models.Model):
    """
    Defines whether the role is under a Club, Committee, or Nodal.
    """
    TYPE_CHOICES = [
        ("Club", "Club"),
        ("Committee", "Committee"),
        ("Nodal", "Nodal"),
    ]
    name = models.CharField(max_length=50, choices=TYPE_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Association(models.Model):
    """
    Represents a specific Club / Committee / Nodal body.
    Example: Eco Club, Examination Committee, Discipline Nodal, etc.
    """
    name = models.CharField(max_length=255)
    type = models.ForeignKey(AssociationType, on_delete=models.CASCADE, related_name="associations")
    school = models.ForeignKey("School", on_delete=models.CASCADE, related_name="associations")

    def __str__(self):
        return f"{self.name} ({self.type.name})"


class AssociationRole(models.Model):
    """
    Role inside an association (like President, Secretary, Coordinator, Member).
    """
    title = models.CharField(max_length=255)
    responsibilities = models.TextField(blank=True, null=True)
    association = models.ForeignKey(Association, on_delete=models.CASCADE, related_name="roles")

    def __str__(self):
        return f"{self.title} - {self.association.name}"


class StaffAssociationRoleAssignment(models.Model):
    """
    Assigns a staff member to a role inside a specific association.
    """
    staff = models.ForeignKey("Staff", on_delete=models.CASCADE, related_name="association_roles")
    role = models.ForeignKey(AssociationRole, on_delete=models.CASCADE, related_name="assigned_staff")
    assigned_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff.name} - {self.role.title} ({self.role.association.name})"



class Event(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.title} ({self.school.name})"

def school_document_path(instance, filename):
    # Save files under documents/<school_name>/<filename>
    return os.path.join("documents", instance.school.name.replace(" ", "_"), filename)

class Document(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name="documents",null=True, blank=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=school_document_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.school.name}"
              
class News(models.Model):
    CATEGORY_CHOICES = [
        ('Academics', 'Academics'),
        ('Events', 'Events'),
        ('Sports', 'Sports'),
        ('Community', 'Community'),
        ('General', 'General'),
    ]
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name="news")
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now, db_index=True)
    # Optional author link
    # author = models.ForeignKey('Staff', on_delete=models.SET_NULL, blank=True, null=True, related_name="news_articles")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, default='General')
    image = models.ImageField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News Article"
        verbose_name_plural = "News"
        ordering = ['-date_published']  # Most recent first


class ExtracurricularActivity(models.Model):
    CATEGORY_CHOICES = [
        ('Sports', 'Sports'),
        ('Clubs', 'Clubs'),
        ('Arts', 'Arts'),
        ('Academic', 'Academic'),
        ('Community Service', 'Community Service'),
        ('Other', 'Other'),
    ]

    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='activities')  # ✅ link activities to a school
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='activity_images/', blank=True, null=True)
    coordinator = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='coordinated_activities')
    participants = models.ManyToManyField('Student', related_name='participated_activities', blank=True)
    requirements = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    registration_link = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.school.name})"

    class Meta:
        verbose_name = "Extracurricular Activity"
        verbose_name_plural = "Extracurricular Activities"
        ordering = ['name']
        
class Committee(models.Model):
    name = models.CharField(max_length=100)
    objectives = models.TextField(blank=True)
    chairperson = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='chaired_committees')
    tasks = models.TextField(blank=True)
    documents = models.ManyToManyField('Document', related_name='committee', blank=True)

    def __str__(self):
        return self.name
    
class CommitteeMember(models.Model):
    committee=models.ManyToManyField('Committee',related_name='CommitteeMember', blank=True)
    member = models.ManyToManyField('Staff', related_name='CommitteeMember', blank=True)
    designation = models.CharField(max_length=50)  
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='smc_members/', blank=True)  # Optional image field

    def __str__(self):
        return self.member

    class Meta:
        ordering = ['designation']

class CommitteeMeeting(models.Model):

    meeting_schedule = models.CharField(max_length=100, blank=True)
    agenda = models.TextField(blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Committee Meeting on {self.meeting_schedule} "
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    head_of_department = models.OneToOneField('Staff',  on_delete=models.SET_NULL, null=True,related_name='Department')

    def __str__(self):
        return self.name
    

    



class SMCMember(models.Model):
    school = models.ForeignKey(
        "School",
        on_delete=models.CASCADE,
        related_name="smc_members"
    )

    POSITION_CHOICES = [
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Member Secretary', 'Member Secretary'),
        ('Trained Education Scholar Member', 'Trained Education Scholar Member'),
        ('Teacher/Student Member', 'Teacher/Student Member'),
        ('Parent/Guardian Member', 'Parent/Guardian Member'),
        ('Member', 'Member'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    CATEGORY_CHOICES = [
        ('GEN', 'General'),
        ('SC', 'Scheduled Caste'),
        ('BC-A', 'Backward Class - A'),
        ('BC-B', 'Backward Class - B'),
        ('EWS', 'Economically Weaker Section'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to='smc_photos/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    # 🔹 New priority field
    priority = models.PositiveIntegerField(default=0, help_text="Lower number = higher priority")

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name_plural = "SMC Members"
        ordering = ['priority', 'position', 'name']



                        



class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    srn = models.CharField(primary_key=True, max_length=11)
    school_code = models.CharField(max_length=20, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    admission_date = models.DateField(blank=True, null=True)
    studentclass = models.CharField(max_length=20, blank=True, null=True)
    stream = models.CharField(max_length=50, blank=True, null=True)
    section = models.CharField(max_length=20, blank=True, null=True)
    roll_number = models.IntegerField(blank=True, null=True)
    admission_number = models.CharField(max_length=20, blank=True, null=True)

    # Personal Info
    full_name_aadhar = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    domicile_of_haryana = models.CharField(max_length=100, blank=True, null=True)

    # Parents / Guardian
    father_full_name_aadhar = models.CharField(max_length=255, blank=True, null=True)
    father_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    mother_full_name_aadhar = models.CharField(max_length=255, blank=True, null=True)
    mother_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)


    # Contact
    father_mobile = models.CharField(max_length=20, blank=True, null=True)
    mother_mobile = models.CharField(max_length=20, blank=True, null=True)


    # Financial
    family_annual_income = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    ifsc = models.CharField(max_length=20, blank=True, null=True)

    # Address
    state = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    block = models.CharField(max_length=100, blank=True, null=True)
    sub_district = models.CharField(max_length=100, blank=True, null=True)
    city_village_town = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    # Subjects
    subjects_opted = models.TextField(blank=True, null=True, help_text="Format: Optional:Math, Compulsory:English")
    subjects = models.TextField(blank=True, null=True)

    caste = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    disability = models.CharField(max_length=255, blank=True, null=True)
    disorder = models.CharField(max_length=100, blank=True, null=True)
    below_poverty_line_certificate_number=models.CharField(max_length=255, blank=True, null=True)
    bpl_certificate_issuing_authority = models.CharField(max_length=255, blank=True, null=True)

    family_id = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return str(self.full_name_aadhar) if self.full_name_aadhar else 'Student {}'.format(self.pk)

    def save(self, *args, **kwargs):
        # --- Normalize category ---
        if self.category:
            normalized = self.category.strip().lower()
            mapping = {
                "sc": "SC",
                "scheduled caste": "SC",
                "gen": "GEN",
                "general": "GEN",
                "bc-a": "BC-A",
                "bca": "BC-A",
                "bc-b": "BC-B",
                "bcb": "BC-B",
                "sbc": "GEN",   # 🔹 Count SBC in General
            }
            self.category = mapping.get(normalized, self.category.upper())

        # --- Normalize subjects_opted ---
        if self.subjects_opted:
            subject_list = str(self.subjects_opted).split(',')
            all_subjects = []

            for subject in subject_list:
                parts = subject.split(':', 1)
                if len(parts) == 2:
                    subject_type, subject_name = parts
                    subject_type = subject_type.strip()
                    subject_name = subject_name.strip()

                    if subject_type in ("Compulsory", "Optional","Optional 1","Optional 2", "NSQF", "Language"):
                        all_subjects.append(subject_name)
                    elif subject_type == "Additional":
                        all_subjects.append(f"Additional: {subject_name}")

            # 🔹 Remove duplicates but preserve order
            seen = {}
            cleaned_subjects = [seen.setdefault(s, s) for s in all_subjects if s not in seen]

            # 🔹 Sort alphabetically (case-insensitive)
            self.subjects = ', '.join(sorted(cleaned_subjects, key=lambda x: x.lower()))
        else:
            self.subjects = None

        # ✅ Always call super().save()
        super().save(*args, **kwargs)



            

        # --- code if want to sort as per given choice ---

        # if self.subjects_opted:
        #     subject_list = self.subjects_opted.split(',')

        #     compulsory_subjects = []
        #     optional_subjects = []
        #     nsqf_subjects = []
        #     additional_subjects = []
        #     language_subjects = []

        #     for subject in subject_list:
        #         parts = subject.split(':', 1)  # prevent ValueError
        #         if len(parts) == 2:
        #             subject_type, subject_name = parts
        #             subject_type = subject_type.strip()
        #             subject_name = subject_name.strip()

        #             if subject_type.lower() == "compulsory":
        #                 compulsory_subjects.append(f"Compulsory: {subject_name}")
        #             elif subject_type.lower() == "optional":
        #                 optional_subjects.append(f"Optional: {subject_name}")
        #             elif subject_type.lower() == "nsqf":
        #                 nsqf_subjects.append(f"NSQF: {subject_name}")
        #             elif subject_type.lower() == "additional":
        #                 additional_subjects.append(f"Additional: {subject_name}")
        #             elif subject_type.lower() == "language":
        #                 language_subjects.append(f"Language: {subject_name}")

        #     # ✅ Define order: Compulsory → Optional → NSQF → Additional → Language
        #     ordered_subjects = compulsory_subjects + optional_subjects + nsqf_subjects + additional_subjects + language_subjects

        #     # Save back to subjects field in correct order
        #     self.subjects = ", ".join(ordered_subjects)




class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()

    def __str__(self):
        return self.title   
          


class Infrastructure(models.Model):
    CATEGORY_CHOICES = [
        ("academic", "Academic Block"),
        ("labs", "Laboratories"),
        ("library", "Library"),
        ("sports", "Sports Facilities"),
        ("activities", "Co-curricular & Activity Rooms"),
        ("admin", "Administrative Block"),
        ("student_welfare", "Student Welfare Facilities"),
        ("transport", "Transport"),
        ("hostel", "Hostel"),
        ("other", "Other Facilities"),
    ]

    school = models.ForeignKey(
        School, 
        on_delete=models.CASCADE, 
        related_name="infrastructures"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    photo = models.ImageField(upload_to="infrastructure/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.school.name}"
  




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

      
class StudentAchievement(models.Model):
    ACHIEVEMENT_TYPE_CHOICES = [ 
        ("sports", "Sports"),
        ("cultural", "Cultural Activity"),
        ("competition", "Competition"),
        ("exam", "Final Exam"),
        ("quiz", "Quiz"),
    ]

    student_name = models.CharField(max_length=200, help_text="Enter student name")
    achievement_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPE_CHOICES)
    event_name = models.CharField(max_length=200, blank=True, null=True, help_text="Name of event/activity/exam")
    rank = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 1st, 2nd, Winner")
    reward_title = models.CharField(max_length=200, blank=True, null=True, help_text="Certificate/Medal/Award Title")
    date = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student_name} - {self.achievement_type} ({self.event_name or self.reward_title})"



class ExamDetail(models.Model):
    achievement = models.OneToOneField(
        StudentAchievement,
        on_delete=models.CASCADE,
        related_name="exam_detail"
    )
    obtained_marks = models.DecimalField(max_digits=7, decimal_places=2)
    total_marks = models.DecimalField(max_digits=7, decimal_places=2)

    @property
    def percentage(self):
        if self.total_marks > 0:
            return round((self.obtained_marks / self.total_marks) * 100, 2)
        return 0

    def __str__(self):
        return f"{self.achievement.student_name} - {self.obtained_marks}/{self.total_marks} ({self.percentage}%)"



class FeeStructure(models.Model):
    student_class = models.ForeignKey("Class", on_delete=models.CASCADE)  
    stream = models.ForeignKey("Stream", on_delete=models.CASCADE, null=True, blank=True)  

    admission_fee = models.DecimalField(max_digits=10, decimal_places=2)
    rcf = models.DecimalField(max_digits=10, decimal_places=2)  
    cwf = models.DecimalField(max_digits=10, decimal_places=2)   
    ccwf = models.DecimalField(max_digits=10, decimal_places=2)  

    def total_fee(self):
        return self.admission_fee + self.rcf + self.cwf + self.ccwf

    def __str__(self):
        if self.stream:
            return f"Fee Structure for {self.student_class} ({self.stream})"
        return f"Fee Structure for {self.student_class}"

class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ("admission", "Admission"),
        ("fees", "Fees & Payments"),
        ("academics", "Academics"),
        ("facilities", "Facilities"),
        ("general", "General"),
    ]

    question = models.CharField(max_length=300, help_text="Enter the FAQ question")
    answer = models.TextField(help_text="Provide the answer for the question")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="general",
        help_text="Select category of FAQ"
    )
    order = models.PositiveIntegerField(default=0, help_text="Order for display (0 = top)")
    is_active = models.BooleanField(default=True, help_text="Show or hide on website")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "category", "id"]

    def __str__(self):
        return self.question
    

class MandatoryPublicDisclosure(models.Model):
    SECTION_CHOICES = [
        ("general_info", "General Information"),
        ("documents", "Documents and Information"),
        ("academics", "Academics"),
        ("staff", "Staff Teaching"),
        ("infrastructure", "Infrastructure"),
    ]

    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    title = models.CharField(max_length=255, help_text="Field Name (e.g., Name of School, Affiliation No.)")
    value = models.TextField(help_text="Content or file URL")

    # Optional for files
    file = models.FileField(upload_to="mandatory_disclosure/", blank=True, null=True)

    order = models.PositiveIntegerField(default=0, help_text="Sorting order")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["section", "order"]
        verbose_name = "Mandatory Public Disclosure"
        verbose_name_plural = "Mandatory Public Disclosures"

    def __str__(self):
        return f"{self.section} - {self.title}"







