from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.examinations.exams.models import (
    Exam,
)


class RankSystem(
    SessionBaseModel
):

    RANK_TYPE_CHOICES = [

        (
            "CLASS",
            "Class Rank",
        ),

        (
            "SECTION",
            "Section Rank",
        ),

        (
            "SCHOOL",
            "School Rank",
        ),

        (
            "GENDER",
            "Gender Rank",
        ),

        (
            "CATEGORY",
            "Category Rank",
        ),
    ]

    RANK_METHOD_CHOICES = [

        (
            "COMPETITION",
            "Competition Ranking",
        ),

        (
            "DENSE",
            "Dense Ranking",
        ),

        (
            "STANDARD",
            "Standard Ranking",
        ),
    ]

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="rank_systems",
    )

    name = models.CharField(
        max_length=200,
    )

    rank_type = models.CharField(

        max_length=20,

        choices=RANK_TYPE_CHOICES,
    )

    rank_method = models.CharField(

        max_length=20,

        choices=RANK_METHOD_CHOICES,

        default="DENSE",
    )

    is_active = models.BooleanField(
        default=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "rank_systems"
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
                    "rank_type",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name=(
                    "unique_rank_system"
                ),
            ),
        ]

    def __str__(self):

        return self.name