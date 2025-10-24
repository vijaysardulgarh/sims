from django.db import models
#from django.contrib.gis.db import models as gis_models

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
