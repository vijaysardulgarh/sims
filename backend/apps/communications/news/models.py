from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class News(
    SchoolBaseModel
):

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True
    )

    summary = models.TextField(
        blank=True
    )

    content = models.TextField()

    featured_image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True
    )

    publish_date = models.DateField()

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "news"

        verbose_name = "News"

        verbose_name_plural = "News"

        ordering = [
            "-publish_date"
        ]

    def __str__(self):

        return self.title