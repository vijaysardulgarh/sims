from django.db import models
from django import forms
from django.utils import timezone
import datetime
import json,os
#from django.contrib.gis.db import models as gis_models
from datetime import date
#from django.contrib.auth.models import AbstractUser


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
    
class Stream(models.Model):
    SCIENCE = 'Science'
    COMMERCE = 'Commerce'
    ARTS = 'Arts'

    STREAM_CHOICES = [
        (SCIENCE, 'Science'),
        (COMMERCE, 'Commerce'),
        (ARTS, 'Arts'),
        # Add more streams as needed
    ]

    name = models.CharField(max_length=100, choices=STREAM_CHOICES, unique=True)
    

    def __str__(self):
        return self.name
    
class Class(models.Model):
    CLASS_CHOICES = [
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
    ('9th', '9th'),
    ('10th', '10th'),
    ('11th', '11th'),
    ('12th', '12th'),
    ('na', 'NA'),
]    
    name = models.CharField(max_length=50, unique=True,choices=CLASS_CHOICES)  # Ensure class name is unique
    school = models.ForeignKey(School, on_delete=models.PROTECT)  # Link to School

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Class'


class Section(models.Model):
    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('na', 'NA'),
        # Add more choices as needed
    ]
    name = models.CharField(max_length=2, choices=SECTION_CHOICES)
    section_class = models.ForeignKey('Class', on_delete=models.PROTECT, related_name='sections')
    section_stream = models.ForeignKey('Stream', on_delete=models.PROTECT, related_name='sections')
    def __str__(self):
        return f"{self.section_class.name} ({self.name})"


class SMCMember(models.Model):
    school = models.ForeignKey(
        "School",
        on_delete=models.CASCADE,
        related_name="smc_members"
    )

    POSITION_CHOICES = [
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Parent/Guardian Member', 'Parent/Guardian Member'),
        ('Member', 'Member'),
        ('Member Secretary', 'Member Secretary'),
        ('Teacher/Student Member', 'Teacher/Student Member'),
        ('Trained Education Scholar Member', 'Trained Education Scholar Member'),
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

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name_plural = "SMC Members"
        ordering = ['position']

class Subject(models.Model):
    NONE = 'None'
    HINDI = 'Hindi'
    ENGLISH = 'English'
    SOCIAL_STUDIES = 'Social Studies'
    SCIENCE = 'Science'
    MATH = 'Math'
    PUNJABI = 'Punjabi'
    COMPUTER = 'Computer'
    HOME_SCIENCE = 'Home Science'
    PHYSICS = 'Physics'
    CHEMISTRY = 'Chemistry'
    ACCOUNT = 'Account'
    BUSINESS = 'Business'
    POLITICAL_SCIENCE = 'Political Science'
    ECONOMICS = 'Economics'
    GEOGRAPHY = 'Geography'
    PSYCHOLOGY = 'Psychology'
    PHYSICAL_EDUCATION = 'Physical Education'
    MUSIC = 'Music'
    AUTOMOBILE = 'Automobile'
    BEAUTY_WELLNESS = 'Beauty & Wellness'
    BIOLOGY = 'Biology'
    SANSKRIT = 'Sanskrit'
    FINEARTS = 'Fine Arts'

    SUBJECT_CHOICES = [
        (NONE, 'None'),
        (HINDI, 'Hindi'),
        (ENGLISH, 'English'),
        (SOCIAL_STUDIES, 'Social Studies'),
        (SCIENCE, 'Science'),
        (MATH, 'Math'),
        (PUNJABI, 'Punjabi'),
        (COMPUTER, 'Computer'),
        (HOME_SCIENCE, 'Home Science'),
        (PHYSICS, 'Physics'),
        (CHEMISTRY, 'Chemistry'),
        (ACCOUNT, 'Account'),
        (BUSINESS, 'Business'),
        (POLITICAL_SCIENCE, 'Political Science'),
        (ECONOMICS, 'Economics'),
        (GEOGRAPHY, 'Geography'),
        (PSYCHOLOGY, 'Psychology'),
        (PHYSICAL_EDUCATION, 'Physical Education'),
        (MUSIC, 'Music'),
        (AUTOMOBILE, 'Automobile'),
        (BEAUTY_WELLNESS, 'Beauty & Wellness'),
        (BIOLOGY, 'Biology'),
        (SANSKRIT, 'Sanskrit'),
        (FINEARTS, 'Fine Arts'),
    ]

    name = models.CharField(max_length=100, choices=SUBJECT_CHOICES, unique=True)

    def __str__(self):
        return self.name


class ClassSubject(models.Model):
    class_info = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    periods_per_week = models.IntegerField()
    # Add fields for subject-specific requirements

    def __str__(self):
        return f"{self.class_info} - {self.subject}"
    


class Staff(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True, blank=True, related_name='staff')

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
    designation = models.CharField(max_length=40, null=True, blank=True)

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
    profile_picture = models.ImageField(upload_to='staff_profile/', null=True, blank=True)

    STAFF_ROLE_CHOICES = [
        ('Administrative', 'Administrative'),
        ('Teaching', 'Teaching'),
        ('Non Teaching', 'Non Teaching'),
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

    def __str__(self):
        return f"{self.name} ({self.employee_id})"

    class Meta:
        verbose_name_plural = "Staff"
        ordering = ["school", "staff_role", "employment_type", "name"]


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ClassIncharge(models.Model):
    teacher_name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    class_alloted = models.ForeignKey(Class, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.teacher_name.name} - {self.classroom.name} - {self.class_alloted} - {self.section}"
    
class TimetableSlot(models.Model):
    
    SEASON_CHOICES = (
        ('winter', 'winter'),
        ('summer', 'Summer'),
        ('other', 'Other'),
        # Add more semesters as needed
    )
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    day = models.CharField(max_length=20, choices=DAY_CHOICES)

    period = models.IntegerField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.period}-{self.day} - {self.start_time} - {self.end_time}"
    


class TimeSlot(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)
    
class DailyTimeSlot(models.Model):
    
    day_choices = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    #period = models.IntegerField(null=True, blank=True)
    day = models.CharField(max_length=10, choices=day_choices,null=True, blank=True)
    start_time = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='start_time')
    end_time = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='end_time')
    

    def __str__(self):
        return f"{self.day} - {self.start_time} - {self.end_time}"
    
    class Meta:
        verbose_name = "Daily Time Slot"
        verbose_name_plural = "Daily Time Slots"


class TeacherSubjectAssignment(models.Model):

    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE,to_field='employee_id')
    maximum_periods_per_teacher = models.PositiveIntegerField()
    periods_per_week = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.teacher.name} - {self.subject} - {self.class_name} ({self.maximum_periods_per_teacher} periods)"



class Timetable(models.Model):

    CLASS_TYPE_CHOICES = (
        ('Regular', 'Regular'),
        ('Assembly', 'Assembly'),
        ('Recess', 'Recess'),
        ('Special', 'Special Event'),
        # Add more types as needed
    )

    
    season = models.ForeignKey(TimetableSlot, on_delete=models.SET_NULL, related_name='timetable_season', null=True, blank=True)
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE,related_name='rrrr')
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='rr')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=10, choices=CLASS_TYPE_CHOICES, default='Regular')
    teachers = models.ManyToManyField(Staff, blank=True,limit_choices_to={'subject__in': models.OuterRef('subject')})
    classrooms = models.ManyToManyField(Classroom, blank=True)
    day = models.ForeignKey(TimetableSlot, on_delete=models.SET_NULL, related_name='timetable_day', null=True, blank=True)
    period = models.ForeignKey(TimetableSlot, on_delete=models.SET_NULL, related_name='timetable_period', null=True, blank=True)
    start_time = models.ForeignKey(TimetableSlot, on_delete=models.SET_NULL, related_name='timetable_start_time', null=True, blank=True)
    end_time = models.ForeignKey(TimetableSlot, on_delete=models.SET_NULL, related_name='timetable_end_time', null=True, blank=True)


    is_mandatory = models.BooleanField(default=True)
 

    def __str__(self):
        return f"{self.day}, {self.start_time} - {self.end_time}: {self.class_name} ({self.section})"


class TimetableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            subject = kwargs['instance'].subject
            if subject:
                self.fields['teachers'].queryset = subject.teachers.all()
                # Adjust the queryset as needed based on your model structure

    class Meta:
        model = Timetable
        fields = '__all__'


class Day(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    name = models.CharField(max_length=20, choices=DAY_CHOICES)

    def __str__(self):
        return self.name




class TimetableEntry(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Link to School
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    slot = models.ForeignKey(TimetableSlot, on_delete=models.CASCADE)
    

    # Optional field for handling absent teachers
    #substitute_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Time Table Entries'
        unique_together = ('section', 'slot')  # Ensure no duplicate entries for section and slot

    def __str__(self):
        return f"{self.section.name} - {self.subject.name} - {self.teacher.name} ({self.slot})"
                        



class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    srn = models.CharField(primary_key=True,max_length=11)
    stream = models.CharField(max_length=50, blank=True, null=True)
    school_code = models.CharField(max_length=20, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    admission_date = models.DateField(blank=True, null=True,)
    studentclass = models.CharField(max_length=20,blank=True, null=True)
    stream = models.CharField(max_length=20,blank=True, null=True)
    section = models.CharField(max_length=20,blank=True, null=True)
    roll_number = models.CharField(max_length=20,blank=True, null=True)
    admission_number = models.CharField(max_length=20,blank=True, null=True)
    full_name_aadhar = models.CharField(max_length=255,blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10,blank=True, null=True)
    aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    domicile_of_haryana = models.CharField(max_length=100, blank=True, null=True)
    father_full_name_aadhar = models.CharField(max_length=255,blank=True, null=True)
    father_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    mother_full_name_aadhar = models.CharField(max_length=255,blank=True, null=True)
    mother_aadhaar_number = models.CharField(max_length=20,blank=True, null=True)
    guardian_full_name_aadhar = models.CharField(max_length=255, blank=True, null=True)
    guardian_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    family_annual_income = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    block = models.CharField(max_length=100, blank=True, null=True)
    sub_district = models.CharField(max_length=100, blank=True, null=True)
    city_village_town = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    father_mobile = models.CharField(max_length=20, blank=True, null=True)
    mother_mobile = models.CharField(max_length=20, blank=True, null=True)
    guardian_mobile = models.CharField(max_length=20, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    ifsc = models.CharField(max_length=20, blank=True, null=True)
    subjects_opted = models.CharField(max_length=255, blank=True, null=True)
    caste = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    disability = models.CharField(max_length=255,blank=True, null=True)
    disorder = models.CharField(max_length=100, blank=True, null=True)
    subjects_opted = models.CharField(max_length=255, blank=True, null=True)
    subjects = models.TextField(blank=True, null=True) 
    bpl_certificate_issuing_authority= models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return str(self.full_name_aadhar) if self.full_name_aadhar else 'Student {}'.format(self.pk)

    def save(self, *args, **kwargs):
        if self.subjects_opted:
            # Split the subjects_opted string into individual subjects
            subject_list = self.subjects_opted.split(',')
            
            # Initialize lists to store optional and compulsory subjects
            optional_subjects = []
            #compulsory_subjects = []
            
            # Iterate through each subject to categorize as optional or compulsory
            for subject in subject_list:
                subject_type, subject_name = subject.split(':')
                if subject_type.strip().startswith('Optional'):
                    optional_subjects.append(subject_name.strip())  # Append to optional subjects list
                #elif subject_type.strip().lower() == 'compulsory':
                   # compulsory_subjects.append(subject_name.strip())  # Append to compulsory subjects list
            
            # Construct a dictionary to store optional and compulsory subjects
            #subjects_dict = {
            #    'optional': optional_subjects,
            #    #'compulsory': compulsory_subjects
            #}
                       
            # Store the dictionary in JSON format in the subjects field
                    
            self.subjects = ', '.join(optional_subjects)
            #self.subjects = json.dumps(optional_subjects)
        
        super().save(*args, **kwargs)

class Topper(models.Model):
    AWARD_TYPE = (
        ('Topper', 'Topper'),
        ('Shining Star', 'Shining Star')
    )

    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    obtained_marks = models.FloatField()
    total_marks = models.FloatField()
    exam_date = models.DateField()
    position = models.PositiveIntegerField()
    reason = models.TextField(null=True, blank=True)
    date_awarded = models.DateField(null=True, blank=True)
    award_type = models.CharField(max_length=20, choices=AWARD_TYPE,null=True) 


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

    POST_TYPE_CHOICES = [
        ('TGT', 'TGT (6th–8th)'),
        ('PGT', 'PGT (9th–12th)'),
        ('NT', 'Non-Teaching'),
    ]
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES)

    designation = models.CharField(max_length=50, null=True, blank=True)  # e.g., PGT English, TGT Punjabi, Clerk
    subject = models.ForeignKey(
        'Subject', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    total_posts = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.school} - {self.get_post_type_display()} {self.designation or ''} ({self.total_posts})"

      


