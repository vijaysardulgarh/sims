from django.db import models

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