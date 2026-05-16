from django.db import models

from apps.staff.models.post_type import PostType


class SanctionedPost(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="sanctioned_posts"
    )

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
        "academics.Subject",
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