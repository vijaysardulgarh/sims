from django.db import models

from apps.staff.post_type.models import PostType

from apps.schools.models import School
from apps.academics.subjects.models import Subject
from apps.core.common.base.models import SchoolBaseModel

class SanctionedPost(SchoolBaseModel):

    post_type = models.ForeignKey(
        PostType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    designation = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    total_posts = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.school} - {self.post_type}"

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "post_type",
                    "designation",
                    "subject"
                ],
                name="unique_sanctioned_post"
            )
        ]