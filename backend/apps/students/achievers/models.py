from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Achiever(
    SchoolBaseModel
):

    # =====================================
    # ACHIEVEMENT RELATION
    # =====================================

    achievement = models.OneToOneField(

        "students.Achievement",

        on_delete=models.CASCADE,

        related_name="achiever",
    )

    # =====================================
    # MARKS
    # =====================================

    obtained_marks = models.DecimalField(

        max_digits=7,

        decimal_places=2,
    )

    total_marks = models.DecimalField(

        max_digits=7,

        decimal_places=2,
    )

    # =====================================
    # PERCENTAGE
    # =====================================

    @property
    def percentage(self):

        if self.total_marks > 0:

            return round(

                (
                    self.obtained_marks
                    / self.total_marks
                ) * 100,

                2
            )

        return 0

    # =====================================
    # META
    # =====================================

    class Meta:

        db_table = "achievers"

        ordering = ["-created_at"]

        verbose_name = "Achiever"

        verbose_name_plural = "Achievers"

    # =====================================
    # STRING REPRESENTATION
    # =====================================

    def __str__(self):

        return (

            f"{self.achievement.student_name} - "

            f"{self.obtained_marks}/{self.total_marks} "

            f"({self.percentage}%)"
        )