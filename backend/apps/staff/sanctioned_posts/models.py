from django.db import models

from apps.staff.post_type.models import PostType
from apps.core.common.base.models import SchoolBaseModel


class SanctionedPost(SchoolBaseModel):

    post_type = models.ForeignKey(
        PostType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sanctioned_posts",
    )

    sanctioned_posts = models.PositiveIntegerField(
        default=0,
    )

    regular_working = models.PositiveIntegerField(
        default=0,
    )

    guest_working = models.PositiveIntegerField(
        default=0,
    )

    hkrnl_working = models.PositiveIntegerField(
        default=0,
    )

    class Meta:

        ordering = [
            "post_type__name",
        ]

        indexes = [
            models.Index(
                fields=[
                    "school",
                    "post_type",
                ]
            ),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "school",
                    "post_type",
                ],
                name="unique_sanctioned_post_per_school",
            ),
        ]

    @property
    def regular_vacancy(self):
        """
        Sanctioned - Regular Working
        """
        return max(
            0,
            self.sanctioned_posts -
            self.regular_working,
        )

    @property
    def net_vacancy(self):
        """
        Sanctioned - Regular Working
        - Guest Working
        - HKRNL Working
        """
        return max(
            0,
            self.sanctioned_posts
            - self.regular_working
            - self.guest_working
            - self.hkrnl_working,
        )

    def __str__(self):
        return str(self.post_type)