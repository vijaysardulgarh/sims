from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.examinations.exams.models import (
    Exam,
)


class BestOfSubject(
    SessionBaseModel
):

    RULE_CHOICES = [

        ("BEST_N", "Best N Subjects"),

        (
            "BEST_LANGUAGE_PLUS_N",
            "Best Language + N Subjects",
        ),

        (
            "MANDATORY_AND_BEST_N",
            "Mandatory Subjects + Best N",
        ),
    ]

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="best_of_subject_rules",
    )

    name = models.CharField(
        max_length=200,
    )

    rule_type = models.CharField(

        max_length=50,

        choices=RULE_CHOICES,
    )

    subject_count = models.PositiveIntegerField(
        default=5,
    )

    is_active = models.BooleanField(
        default=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "best_of_subjects"
        )

        ordering = [
            "name",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "academic_session",
                    "exam",
                    "name",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name=(
                    "unique_best_of_subject_rule"
                ),
            ),
        ]

    def __str__(self):

        return self.name