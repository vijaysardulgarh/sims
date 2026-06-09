from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel
)

from apps.associations.associations.models import (
    Association
)


class AssociationRole(
    SessionBaseModel
):

    association = models.ForeignKey(

        Association,

        on_delete=models.CASCADE,

        related_name="roles"
    )

    title = models.CharField(
        max_length=255
    )

    responsibilities = models.TextField(
        blank=True
    )

    class Meta:

        verbose_name = "Association Role"

        verbose_name_plural = (
            "Association Roles"
        )

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "association",
                    "title"
                ],

                name=
                "unique_role_per_association"
            )

        ]

        ordering = [
            "title"
        ]

    def __str__(self):

        return (

            f"{self.title}"

            f" - "

            f"{self.association.name}"
        )