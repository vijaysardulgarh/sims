from django.db import models
from django.core.exceptions import ValidationError
import os
import uuid


# -------------------------
# CONSTANTS
# -------------------------
ALLOWED_TYPES = {"pdf", "doc", "docx", "jpg", "jpeg", "png"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB


def school_document_path(instance, filename):
    parts = filename.rsplit(".", 1)
    ext = parts[1].lower() if len(parts) == 2 else "bin"

    filename = f"{uuid.uuid4()}.{ext}"
    school_id = instance.school_id or "unknown"

    return os.path.join("documents", f"school_{school_id}", filename)


class Document(models.Model):
    school = models.ForeignKey(
        "School",
        on_delete=models.CASCADE,
        related_name="documents",
        db_index=True
    )

    title = models.CharField(max_length=255, db_index=True)

    file = models.FileField(
        upload_to=school_document_path,
        null=False,
        blank=False
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    file_size = models.PositiveIntegerField(null=True, blank=True)
    file_type = models.CharField(max_length=20, blank=True)

    # -------------------------
    # VALIDATION
    # -------------------------
    def clean(self):
        if not self.file:
            return

        # Size validation
        if self.file.size > MAX_FILE_SIZE:
            raise ValidationError("File size must be under 5MB")

        # Extension validation
        name = getattr(self.file, "name", "")
        parts = name.rsplit(".", 1)
        ext = parts[1].lower() if len(parts) == 2 else ""

        if ext not in ALLOWED_TYPES:
            raise ValidationError(f"Unsupported file type: {ext}")

    # -------------------------
    # SAVE
    # -------------------------
    def save(self, *args, **kwargs):
        update_fields = kwargs.get("update_fields")

        file_being_updated = (
            self.file and (update_fields is None or "file" in update_fields)
        )

        # Delete old file safely
        if self.pk and file_being_updated:
            old = type(self).objects.filter(pk=self.pk).only("file").first()
            if old and old.file and old.file.name != self.file.name:
                old.file.delete(save=False)

        # Update metadata
        if file_being_updated:
            self.file_size = self.file.size

            name = getattr(self.file, "name", "")
            parts = name.rsplit(".", 1)
            self.file_type = parts[1].lower() if len(parts) == 2 else ""

        self.full_clean()
        super().save(*args, **kwargs)

    # -------------------------
    # DELETE
    # -------------------------
    def delete(self, *args, **kwargs):
        if self.file:
            self.file.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.school.name})"

    class Meta:
        indexes = [
            models.Index(fields=["school"]),
            models.Index(fields=["title"]),
        ]
        ordering = ["-uploaded_at"]