from django.db import models

class Achiever(models.Model):
    achievement = models.OneToOneField(
        "students.Achievement",
        on_delete=models.CASCADE,
        related_name="students_Achievement"
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