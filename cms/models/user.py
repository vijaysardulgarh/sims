from django.contrib.auth.models import AbstractUser
from django.db import models
from .school import School

class User(AbstractUser):

    role = models.CharField(
        max_length=50,
        choices=[
            ("principal", "Principal"),
            ("teacher", "Teacher"),
            ("clerk", "Clerk"),
            ("student", "Student"),
            ("admin", "Admin"),
        ],
        default="teacher",
    )

    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, null=True, blank=True, related_name="users"
    )

    def __str__(self):
        school_name = self.school.name if self.school else "No School"
        return f"{self.username} ({school_name} - {self.role})"

