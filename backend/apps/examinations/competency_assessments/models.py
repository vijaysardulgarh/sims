from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.examinations.exams.models import (
    Exam,
)

from apps.students.profiles.models import (
    Student,
)

from apps.academics.subjects.models import (
    Subject,
)


class CompetencyAssessment(
    SessionBaseModel
):

    GRADE_CHOICES = [

        ("EXCELLENT", "Excellent"),

        ("GOOD", "Good"),

        ("SATISFACTORY", "Satisfactory"),

        (
            "NEEDS_IMPROVEMENT",
            "Needs Improvement",
        ),
    ]

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="competency_assessments",
    )

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="competency_assessments",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.CASCADE,

        related_name="competency_assessments",
    )

    knowledge_grade = models.CharField(

        max_length=30,

        choices=GRADE_CHOICES,
    )

    understanding_grade = models.CharField(

        max_length=30,

        choices=GRADE_CHOICES,
    )

    application_grade = models.CharField(

        max_length=30,

        choices=GRADE_CHOICES,
    )

    analysis_grade = models.CharField(

        max_length=30,

        choices=GRADE_CHOICES,
    )

    communication_grade = models.CharField(

        max_length=30,

        choices=GRADE_CHOICES,
    )

    creativity_grade = models.CharField(

        max_length=30,

        choices=GRADE_CHOICES,
    )

    teacher_remark = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "competency_assessments"
        )

        ordering = [
            "-created_at",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "student",
                    "exam",
                    "subject",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name=(
                    "unique_competency_assessment"
                ),
            ),
        ]

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.subject}"
        )