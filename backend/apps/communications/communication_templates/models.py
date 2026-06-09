from django.db import models

from apps.communications.communication_categories.models import (
    CommunicationCategory
)

from apps.core.common.base.models import (
    SchoolBaseModel
)


class CommunicationTemplate(
    SchoolBaseModel
):

    category = models.ForeignKey(
        CommunicationCategory,
        on_delete=models.CASCADE,
        related_name="templates"
    )

    name = models.CharField(
        max_length=200
    )

    subject = models.CharField(
        max_length=255
    )

    content = models.TextField()

    class Meta:

        db_table = "communication_templates"

        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["school", "name"],
                name="unique_template_name_per_school"
            )
        ]

    def __str__(self):

        return self.name