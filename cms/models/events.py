from django.db import models
from django.utils import timezone
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