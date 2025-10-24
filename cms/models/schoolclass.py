from django.db import models
from .school import School


class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classes")
    name = models.CharField(max_length=50)  # e.g., "9th"
    class_order = models.PositiveIntegerField(default=0)  # numeric ordering

    class Meta:
        unique_together = ('school', 'name')
        ordering = ['class_order', 'name']

    def __str__(self):
        return f"{self.name}"
    

class Stream(models.Model):

    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="streams")

    class Meta:
        unique_together = ('school', 'name')

    def __str__(self):
        return f"{self.name}"
    
class Medium(models.Model):
    name = models.CharField(max_length=50)  # e.g., English, Hindi, Punjabi
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="mediums")

    class Meta:
        unique_together = ('school', 'name')

    def __str__(self):
        return f"{self.name}"

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classrooms")
    name = models.CharField(max_length=20)   # e.g., R101, Block A-2
    capacity = models.PositiveIntegerField(default=40)
    floor = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = ('school', 'name')

    def __str__(self):
        return f"Room {self.name}"
    
            
class Section(models.Model):


    SUB_STREAM_CHOICES = [
        ("Medical", "Medical"),
        ("Non-Medical", "Non-Medical"),
        ("Vocational", "Vocational"),
    ]
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="sections")
    sec_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="sections")
    name = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name="sections")
    medium = models.ForeignKey(Medium, on_delete=models.SET_NULL, null=True, blank=True, related_name="sections")
    stream = models.ForeignKey(Stream, on_delete=models.SET_NULL, null=True, blank=True, related_name="sections")
    sub_stream = models.CharField(max_length=100, choices=SUB_STREAM_CHOICES, null=True, blank=True)

    class Meta:
        unique_together = ('school','sec_class', 'name', 'medium', 'stream', 'sub_stream')

    def __str__(self):
        base = f"{self.sec_class.name} {self.name}"
        if self.stream:
            base += f" ({self.stream.name})"
        if self.sub_stream:
            base += f" - {self.sub_stream}"
        if self.medium:
            base += f" - {self.medium.name}"
        return base    