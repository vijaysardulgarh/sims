from django.db import models, transaction
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify


# -----------------------------------------------------------------------------
# BASE MIXIN (Reusable for all models)
# -----------------------------------------------------------------------------

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey("Staff", null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    updated_by = models.ForeignKey("Staff", null=True, blank=True, on_delete=models.SET_NULL, related_name="+")

    class Meta:
        abstract = True


# -----------------------------------------------------------------------------
# ASSOCIATION
# -----------------------------------------------------------------------------

class Association(BaseModel):

    TYPE_CHOICES = [
        ("Club", "Club"),
        ("Committee", "Committee"),
        ("Nodal", "Nodal"),
    ]

    school = models.ForeignKey("School", on_delete=models.CASCADE, related_name="associations", db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    association_type = models.CharField(max_length=20, choices=TYPE_CHOICES, db_index=True)

    chairperson = models.ForeignKey(
        'Staff',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='chaired_associations'
    )

    tasks = models.TextField(blank=True)
    documents = models.ManyToManyField('Document', related_name='associations', blank=True)

    show_on_website = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    slug = models.SlugField(blank=True, db_index=True)

    class Meta:
        verbose_name = "Association"
        verbose_name_plural = "Associations"
        constraints = [
            models.UniqueConstraint(fields=["school", "slug"], name="unique_association_slug_per_school"),
            models.UniqueConstraint(fields=["school", "name"], name="unique_association_name_per_school"),
        ]
        indexes = [
            models.Index(fields=["school", "association_type"]),
        ]
        ordering = ["name"]

    def clean(self):
        if self.chairperson and self.chairperson.school != self.school:
            raise ValidationError("Chairperson must belong to same school")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)

            with transaction.atomic():
                slug = base_slug
                counter = 1

                while Association.objects.select_for_update().filter(
                    school=self.school, slug=slug
                ).exclude(pk=self.pk).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1

                self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.association_type})"


# -----------------------------------------------------------------------------
# ASSOCIATION ROLES
# -----------------------------------------------------------------------------

class AssociationRole(BaseModel):

    association = models.ForeignKey(Association, on_delete=models.CASCADE, related_name="roles", db_index=True)
    title = models.CharField(max_length=255)
    responsibilities = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Association Role"
        verbose_name_plural = "Association Roles"
        constraints = [
            models.UniqueConstraint(fields=["association", "title"], name="unique_role_per_association")
        ]
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} - {self.association.name}"


# -----------------------------------------------------------------------------
# STAFF ROLE ASSIGNMENT
# -----------------------------------------------------------------------------

class StaffAssociationRoleAssignment(BaseModel):

    staff = models.ForeignKey("Staff", on_delete=models.CASCADE, related_name="association_roles", db_index=True)
    role = models.ForeignKey(AssociationRole, on_delete=models.CASCADE, related_name="assigned_staff", db_index=True)

    class Meta:
        verbose_name = "Staff Role Assignment"
        verbose_name_plural = "Staff Role Assignments"
        constraints = [
            models.UniqueConstraint(fields=["staff", "role"], name="unique_staff_role")
        ]

    def clean(self):
        if self.staff.school != self.role.association.school:
            raise ValidationError("Staff must belong to same school")

    def __str__(self):
        return f"{self.staff.name} - {self.role.title} ({self.role.association.name})"


# -----------------------------------------------------------------------------
# STUDENT ROLE ASSIGNMENT
# -----------------------------------------------------------------------------

class StudentAssociationRoleAssignment(BaseModel):

    student = models.ForeignKey("Student", on_delete=models.CASCADE, related_name="association_roles", db_index=True)
    role = models.ForeignKey(AssociationRole, on_delete=models.CASCADE, related_name="assigned_students", db_index=True)

    class Meta:
        verbose_name = "Student Role Assignment"
        verbose_name_plural = "Student Role Assignments"
        constraints = [
            models.UniqueConstraint(fields=["student", "role"], name="unique_student_role")
        ]

    def clean(self):
        if self.student.school != self.role.association.school:
            raise ValidationError("Student must belong to same school")

    def __str__(self):
        return f"{self.student.full_name_aadhar} - {self.role.title} ({self.role.association.name})"


# -----------------------------------------------------------------------------
# ASSOCIATION MEMBERS
# -----------------------------------------------------------------------------

class AssociationMember(BaseModel):

    association = models.ForeignKey(Association, on_delete=models.CASCADE, related_name='members', db_index=True)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='association_memberships', db_index=True)

    designation = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='association_members/', blank=True)

    class Meta:
        verbose_name = "Association Member"
        verbose_name_plural = "Association Members"
        constraints = [
            models.UniqueConstraint(fields=["association", "staff"], name="unique_member")
        ]
        ordering = ['designation', 'staff__name']

    def clean(self):
        if self.staff.school != self.association.school:
            raise ValidationError("Staff must belong to same school")

    def __str__(self):
        return f"{self.staff.name} ({self.designation}) - {self.association.name}"


# -----------------------------------------------------------------------------
# MEETINGS
# -----------------------------------------------------------------------------

class AssociationMeeting(BaseModel):

    association = models.ForeignKey('Association', on_delete=models.CASCADE, related_name='meetings', db_index=True)
    meeting_date = models.DateTimeField(null=True, blank=True, db_index=True)
    agenda = models.TextField(blank=True)
    location = models.CharField(max_length=100)

    minutes_document = models.ForeignKey(
        'Document',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Association Meeting"
        verbose_name_plural = "Association Meetings"
        ordering = ['-meeting_date']
        indexes = [
            models.Index(fields=["association", "meeting_date"]),
        ]

    def __str__(self):
        return f"{self.association.name} Meeting on {self.meeting_date}"


# -----------------------------------------------------------------------------
# SMC
# -----------------------------------------------------------------------------

class SMCMember(BaseModel):

    school = models.ForeignKey("School", on_delete=models.CASCADE, related_name="smc_members", db_index=True)

    POSITION_CHOICES = [
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Member Secretary', 'Member Secretary'),
        ('Member', 'Member'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)

    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    priority = models.PositiveIntegerField(default=0)
    show_on_website = models.BooleanField(default=True)

    class Meta:
        verbose_name = "SMC Member"
        verbose_name_plural = "SMC Members"
        ordering = ['priority', 'name']

    def __str__(self):
        return f"{self.name} - {self.position}"


# -----------------------------------------------------------------------------
# ACTIVITIES
# -----------------------------------------------------------------------------

class ExtracurricularActivity(BaseModel):

    CATEGORY_CHOICES = [
        ('Sports', 'Sports'),
        ('Clubs', 'Clubs'),
        ('Arts', 'Arts'),
        ('Academic', 'Academic'),
        ('Community Service', 'Community Service'),
        ('Other', 'Other'),
    ]

    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='activities', db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, db_index=True)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    location = models.CharField(max_length=255, blank=True)

    coordinator = models.ForeignKey(
        'Staff',
        on_delete=models.SET_NULL,
        null=True,
        related_name='coordinated_activities'
    )

    participants = models.ManyToManyField('Student', related_name='participated_activities', blank=True)

    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Extracurricular Activity"
        verbose_name_plural = "Extracurricular Activities"
        ordering = ['name']
        indexes = [
            models.Index(fields=["school", "category"]),
        ]

    def clean(self):
        if self.coordinator and self.coordinator.school != self.school:
            raise ValidationError("Coordinator must belong to same school")

        if self.end_date and self.start_date and self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date")

        if self.capacity and self.capacity < 1:
            raise ValidationError("Capacity must be at least 1")

    def __str__(self):
        return f"{self.name} ({self.school.name})"