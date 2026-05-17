from django.db import models

from apps.core.schools.models import School

from apps.core.users.models import User


class MediaFile(models.Model):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="media_files"
    )

    file = models.FileField(
        upload_to="media/"
    )

    file_type = models.CharField(
        max_length=50
    )

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.file.name