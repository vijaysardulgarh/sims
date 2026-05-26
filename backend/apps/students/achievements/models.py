from django.db import models

from apps.core.common.base.models import SchoolBaseModel


class Achievement(
    SchoolBaseModel
):

    # =====================================
    # ACHIEVEMENT TYPE CHOICES
    # =====================================

    ACHIEVEMENT_TYPE_CHOICES = [

        ("sports", "Sports"),

        ("cultural", "Cultural Activity"),

        ("competition", "Competition"),

        ("exam", "Final Exam"),

        ("quiz", "Quiz"),
    ]

    # =====================================
    # STUDENT DETAILS
    # =====================================

    student_name = models.CharField(

        max_length=200,

        help_text="Enter student name",
    )

    # =====================================
    # ACHIEVEMENT DETAILS
    # =====================================

    achievement_type = models.CharField(

        max_length=20,

        choices=ACHIEVEMENT_TYPE_CHOICES,
    )

    event_name = models.CharField(

        max_length=200,

        blank=True,

        null=True,

        help_text="Name of event/activity/exam",
    )

    rank = models.CharField(

        max_length=50,

        blank=True,

        null=True,

        help_text="Example: 1st, 2nd, Winner",
    )

    reward_title = models.CharField(

        max_length=200,

        blank=True,

        null=True,

        help_text="Certificate/Medal/Award Title",
    )

    date = models.DateField()

    remarks = models.TextField(

        blank=True,

        null=True,
    )

    # =====================================
    # META
    # =====================================

    class Meta:

        db_table = "achievements"

        ordering = ["-date"]

        verbose_name = "Achievement"

        verbose_name_plural = "Achievements"

    # =====================================
    # STRING REPRESENTATION
    # =====================================

    def __str__(self):

        return (

            f"{self.student_name} - "

            f"{self.get_achievement_type_display()} "

            f"({self.event_name or self.reward_title})"
        )