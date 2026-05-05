from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Q
from .school import School
from .utils import generate_unique_slug


class AboutSchool(models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE, related_name='about')

    history = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)

    def __str__(self):
        return f"About {self.school.name}"


class Principal(models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE, related_name='principal')

    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="principal/", blank=True, null=True)
    message = models.TextField()

    def clean(self):
        if self.name:
            self.name = self.name.strip()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Principal {self.name} ({self.school.name})"


class Affiliation(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='affiliations', db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def clean(self):
        if self.name:
            self.name = self.name.strip()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "name"], name="unique_affiliation_per_school")
        ]
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.school.name}"


class Infrastructure(models.Model):
    CATEGORY_CHOICES = [
        ("academic", "Academic Block"),
        ("labs", "Laboratories"),
        ("library", "Library"),
        ("sports", "Sports Facilities"),
        ("activities", "Co-curricular"),
        ("admin", "Administrative"),
        ("student_welfare", "Student Welfare"),
        ("transport", "Transport"),
        ("hostel", "Hostel"),
        ("other", "Other"),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="infrastructures", db_index=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    photo = models.ImageField(upload_to="infrastructure/", blank=True, null=True)

    def clean(self):
        if self.title:
            self.title = self.title.strip()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=["school", "category"]),
        ]

    def __str__(self):
        return f"{self.title} - {self.school.name}"


class MandatoryPublicDisclosure(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="disclosures", db_index=True)

    SECTION_CHOICES = [
        ("general_info", "General Information"),
        ("documents", "Documents"),
        ("academics", "Academics"),
        ("staff", "Staff"),
        ("infrastructure", "Infrastructure"),
    ]

    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    title = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    file = models.FileField(upload_to="mandatory_disclosure/", blank=True, null=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def clean(self):
        if self.title:
            self.title = self.title.strip()

        clean_value = (self.value or "").strip()

        if not clean_value and not self.file:
            raise ValidationError("Either value or file must be provided")

        self.value = clean_value

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["school", "section", "title"],
                name="unique_disclosure_per_school"
            ),
            models.CheckConstraint(
                check=~((Q(value="") | Q(value__isnull=True)) & Q(file__isnull=True)),
                name="disclosure_value_or_file_required"
            ),
        ]
        ordering = ["section", "order"]
        indexes = [
            models.Index(fields=["school", "section"]),
        ]

    def __str__(self):
        return f"{self.section} - {self.title}"


class Facility(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="facilities", db_index=True)

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='facility_images/', blank=True, null=True)

    def clean(self):
        if self.name:
            self.name = self.name.strip()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "name"], name="unique_facility_per_school")
        ]
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.school.name})"


class Event(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="events", db_index=True)

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def clean(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-start_date"]
        indexes = [
            models.Index(fields=["school", "start_date"]),
        ]

    def __str__(self):
        return f"{self.title} ({self.school.name})"


class News(models.Model):
    CATEGORY_CHOICES = [
        ('Academics', 'Academics'),
        ('Events', 'Events'),
        ('Sports', 'Sports'),
        ('Community', 'Community'),
        ('General', 'General'),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="news", db_index=True)

    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, db_index=True)

    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now, db_index=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='General')
    image = models.ImageField(upload_to='news/', blank=True, null=True)

    def clean(self):
        if self.title:
            self.title = self.title.strip()

        if self.slug:
            self.slug = self.slug.strip().lower()

    def save(self, *args, **kwargs):
        self.full_clean()

        if not self.slug:
            qs = News.objects.filter(school=self.school)
            if self.pk:
                qs = qs.exclude(pk=self.pk)

            self.slug = generate_unique_slug(News, self.title, queryset=qs)

        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "slug"], name="unique_news_slug")
        ]
        indexes = [
            models.Index(fields=["school", "date_published"]),
            models.Index(fields=["school", "slug"]),
        ]
        ordering = ['-date_published']

    def __str__(self):
        return self.title


class FAQ(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="faqs", db_index=True)

    CATEGORY_CHOICES = [
        ("admission", "Admission"),
        ("fees", "Fees"),
        ("academics", "Academics"),
        ("facilities", "Facilities"),
        ("general", "General"),
    ]

    question = models.CharField(max_length=300)
    answer = models.TextField()

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="general")

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.question:
            self.question = self.question.strip()
        if self.answer:
            self.answer = self.answer.strip()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "question"], name="unique_faq_per_school")
        ]
        ordering = ["order", "category"]
        indexes = [
            models.Index(fields=["school", "category"]),
        ]

    def __str__(self):
        return self.question