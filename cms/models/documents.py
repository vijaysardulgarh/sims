from django.db import models
import os
def school_document_path(instance, filename):
    # Save files under documents/<school_name>/<filename>
    return os.path.join("documents", instance.school.name.replace(" ", "_"), filename)

class Document(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name="documents",null=True, blank=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=school_document_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.school.name}"