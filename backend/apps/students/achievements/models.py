from django.db import models


class Achievement(models.Model):
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